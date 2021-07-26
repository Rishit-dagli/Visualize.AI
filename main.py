import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt
from skimage.transform import resize
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications import EfficientNetB4
from tensorflow.keras.applications import MobileNetV2
import json
import random
import string

from google.cloud import storage

bucket_name = "postmanhack"

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def upload_blob(bucket_name, filename, dest_filename):
    """Uploads a file to the bucket."""
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(dest_filename)
    try:
        blob.delete()
    except:
        pass
    blob.upload_from_filename(filename)
    blob.make_public()
    return blob.public_url


def viz_grad_cam(model, image, interpolant=0.5):
    """VizGradCAM - Displays GradCAM based on Keras / TensorFlow models
    using the gradients from the last convolutional layer. This function
    should work with all Keras Application listed here:
    https://keras.io/api/applications/
    Parameters:
    model (keras.model): Compiled Model with Weights Loaded
    image: Image to Perform Inference On
    plot_results (boolean): True - Function Plots using PLT
                            False - Returns Heatmap Array
    Returns:
    Heatmap Array?
    """
    
    # Sanity Check
    assert (
            0 < interpolant < 1
    ), "Heatmap Interpolation Must Be Between 0 - 1"

    last_conv_layer = next(
        x for x in model.layers[::-1] if isinstance(x, tf.keras.layers.Conv2D)
    )
    target_layer = model.get_layer(last_conv_layer.name)

    original_img = image
    img = np.expand_dims(original_img, axis=0)
    prediction = model.predict(img)

    # Obtain Prediction Index
    prediction_idx = np.argmax(prediction)

    # Compute Gradient of Top Predicted Class
    with tf.GradientTape() as tape:
        gradient_model = Model([model.inputs], [target_layer.output, model.output])
        conv2d_out, prediction = gradient_model(img)
        # Obtain the Prediction Loss
        loss = prediction[:, prediction_idx]

    # Gradient() computes the gradient using operations recorded
    # in context of this tape
    gradients = tape.gradient(loss, conv2d_out)

    # Obtain the Output from Shape [1 x H x W x CHANNEL] -> [H x W x CHANNEL]
    output = conv2d_out[0]

    # Obtain Depthwise Mean
    weights = tf.reduce_mean(gradients[0], axis=(0, 1))

    # Create a 7x7 Map for Aggregation
    activation_map = np.zeros(output.shape[0:2], dtype=np.float32)

    # Multiply Weights with Every Layer
    for idx, weight in enumerate(weights):
        activation_map += weight * output[:, :, idx]

    # Resize to Size of Image
    activation_map = cv2.resize(
        activation_map.numpy(), (original_img.shape[1], original_img.shape[0])
    )

    # Ensure No Negative Numbers
    activation_map = np.maximum(activation_map, 0)

    # Convert Class Activation Map to 0 - 255
    activation_map = (activation_map - activation_map.min()) / (
        activation_map.max() - activation_map.min()
    )
    activation_map = np.uint8(255 * activation_map)

    # Convert to Heatmap
    heatmap = cv2.applyColorMap(activation_map, cv2.COLORMAP_JET)

    # Superimpose Heatmap on Image Data
    original_img = np.uint8(
        (original_img - original_img.min())
        / (original_img.max() - original_img.min())
        * 255
    )

    cvt_heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)

    # Enlarge Plot
    plt.rcParams["figure.dpi"] = 100

    final_image = np.uint8(original_img * interpolant + cvt_heatmap * (1 - interpolant))
    plt.imsave("/tmp/finalimage.png", final_image)

    return True


def conv_vis(request):
    global bucket_name

    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and "image" in request_json:
        url = request_json["image"]
    elif request_args and "image" in request_args:
        url = request_args["image"]
    else:
        url = "https://i.imgur.com/taUKyu1.jpg"

    print(url)

    if request_json and "destination" in request_json:
        dest = request_json["destination"]
    elif request_args and "destination" in request_args:
        dest = request_args["destination"]
    else:
        dest = random_char(7) + ".png"

    image_path = tf.keras.utils.get_file("/tmp/image.png", url)
    test_img = img_to_array(load_img(image_path, target_size=(224, 224)))

    viz_grad_cam(MobileNetV2(weights="imagenet"), test_img)  # load model

    public_url = upload_blob(bucket_name, "/tmp/finalimage.png", dest)

    response = {}
    response['output_image'] = public_url
    response = json.dumps(response)

    return response
