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

## Want to Contribute 🙋‍♂️?

Awesome! If you want to contribute to this project, you're always welcome! See [Contributing Guidelines](CONTRIBUTING.md). You can also take a look at [Visualize.AI's Project Issues](https://github.com/Rishit-dagli/Visualize.AI/issues) for getting more information about current or upcoming tasks.

## Want to discuss? 💬

Have any questions, doubts or want to present your opinions, views? You're always welcome. You can [start discussions](https://github.com/Rishit-dagli/Visualize.AI/discussions).

## Citations

```bibtex
@misc{hughes2016open,
      title={An open access repository of images on plant health to enable the development of mobile disease diagnostics}, 
      author={David. P. Hughes and Marcel Salathe},
      year={2016},
      eprint={1511.08060},
      archivePrefix={arXiv},
      primaryClass={cs.CY}
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

