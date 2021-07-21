# Visualize.AI

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/rishitdagli/workspace/visualizing-an-ml-model/overview)
[![Lint Code Base](https://github.com/Rishit-dagli/Visualize.AI/actions/workflows/linter.yml/badge.svg)](https://github.com/Rishit-dagli/Visualize.AI/actions/workflows/linter.yml)
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

## Lint ✅

This project uses [***GitHub Super Linter***](https://github.com/github/super-linter) which is Combination of multiple linters to install as a GitHub Action.

Following Linters are used internally by super linter (enabled for this project):
- Python: [Black](https://github.com/psf/black)
- YAML: [YamlLint](https://github.com/adrienverge/yamllint)
