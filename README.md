# Visualize.AI

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/rishitdagli/workspace/visualizing-an-ml-model/overview)
[![Lint Code Base](https://github.com/Rishit-dagli/Visualize.AI/actions/workflows/linter.yml/badge.svg?branch=main)](https://github.com/Rishit-dagli/Visualize.AI/actions/workflows/linter.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Rishit-dagli/Visualize.AI?style=social)](https://github.com/Rishit-dagli/Visualize.AI/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Rishit-dagli/Visualize.AI?style=social)](https://github.com/Rishit-dagli/Visualize.AI/network/members)

This repo creates an API to better understand and visualize the inner workings 
of a CNN with GradCam; currently MobileNet powered by TensorFlow and Google 
Cloud Functions. This also shows using the Postman Visualizer to make sense of 
the API responses and visualize the journey of an image in the model.

## Run Locally

To get up and running with this API, run the following commands, make sure you 
have Python installed. This runs the function in built-in local development 
server:

```
git clone https://github.com/Rishit-dagli/Visualize.AI # or clone your own fork
cd Visualize.AI
pip install -r requirements.txt
functions-framework-python --target conv_vis
# Can also use --debug
```

Your function should now be running on localhost:8080 🚀.

## About the API📝

This API was deployed on GCP Cloud Functions and is extremely easy to deploy 
your own such API. You can simply deploy it to your own Cloud Function with 
this command:

```sh
gcloud functions deploy conv_vis --runtime python38 --memory 8196MB --trigger-http --allow-unauthenticated
```

Or even do this with the Google Cloud GUI.

### Using the API

#### Endpoint URL

```
https://us-central1-sound-fastness-257416.cloudfunctions.net
```

#### Request Params

| Key         | Description                                                                     |
|-------------|---------------------------------------------------------------------------------|
| image       | URL of the image you put in the model                                           |
| destination | File name of the destination image, remember to use extension (.png , .jpg etc) |


#### Just want to test out?

I got you covered, I have added an example image as the default value for you to try out here are the default values:

| Key         | Default Value                   |
|-------------|---------------------------------|
| image       | https://i.imgur.com/taUKyu1.jpg |
| destination | A random string                 |

## Lint ✅

This project uses [***GitHub Super Linter***](https://github.com/github/super-linter) which is Combination of multiple linters to install as a GitHub Action.

Following Linters are used internally by super linter (enabled for this project):
- Python: [Black](https://github.com/psf/black)
- YAML: [YamlLint](https://github.com/adrienverge/yamllint)

## Want to Contribute 🙋‍♂️?

Awesome! If you want to contribute to this project, you're always welcome! See [Contributing Guidelines](CONTRIBUTING.md). You can also take a look at [Visualize.AI's Project Issues](https://github.com/Rishit-dagli/Visualize.AI/issues) for getting more information about current or upcoming tasks.

## Want to discuss? 💬

Have any questions, doubts or want to present your opinions, views? You're always welcome. You can [start discussions](https://github.com/Rishit-dagli/Visualize.AI/discussions).

## Citations

```bibtex
@article{Selvaraju_2019,
   title={Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization},
   volume={128},
   ISSN={1573-1405},
   url={http://dx.doi.org/10.1007/s11263-019-01228-7},
   DOI={10.1007/s11263-019-01228-7},
   number={2},
   journal={International Journal of Computer Vision},
   publisher={Springer Science and Business Media LLC},
   author={Selvaraju, Ramprasaath R. and Cogswell, Michael and Das, Abhishek and Vedantam, Ramakrishna and Parikh, Devi and Batra, Dhruv},
   year={2019},
   month={Oct},
   pages={336–359}
}
```

## License

```
Copyright 2020 Rishit Dagli

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

