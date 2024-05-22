# twinLab Tutorials

<p align="center">
    <!-- <img src="./resources/images/logo.svg" width="200" height="200" /> -->
    <img src="./resources/images/twinLab.svg" width="200" height="200"/>
</p>

![digiLab](./resources/images/digiLab_badge.svg) ![twinLab](./resources/images/twinLab_badge.svg) [![slack](https://img.shields.io/badge/slack-@digilabglobal-purple.svg?logo=slack)](https://digilabglobal.slack.com)

## Welcome

Welcome to the twinLab-Tutorials repository, brought to you by the twinLab Product Team at digiLab Solutions Ltd. This repository contains Jupyter Notebooks that can serve as a starting point for using twinLab, a tool to augment engineering workflows with probabilistic machine learning.

If you would like to access a trial of twinLab to harness the power of built-in uncertainty quantification and build real-time emulators of your simulations, please [sign up for a trial here](https://www.digilab.co.uk/contact).

twinLab can be accessed through [PyPi](https://pypi.org/project/twinlab/), or through [GitHub](https://github.com/digiLab-ai/twinLab-Interface). Please feel free to log an issue on our public GitHub if you have a feature request or a bug report, or contact the Product Team at twinlab@digilab.co.uk. Documentation and guidance on how to use twinLab can be found via our [documentation](https://twinlab.ai/).

Similarly, if you spot an error in our tutorials, please feel free to log an issue in this GitHub repository, or contact the Product Team.

## Quick Start

Clone the repository and change directory to the project root:

```shell
git clone https://github.com/digiLab-ai/twinLab-Tutorials.git
cd twinLab-Tutorials
```

Install the dependencies:

```shell
poetry install --no-root
```

Copy the `.env.example` file to `.env`:

```shell
cp .env.example .env
```

Ensure that you fill out your `twinLab` login details in `.env`.

Finally, run the notebook you would like to see, e.g. [Quickstart](./notebooks/Quickstart.ipynb):

```shell
poetry run jupyter notebook notebooks/Quickstart.ipynb
```

You can find additional resources to run the notebooks in the [resources](./resources/datasets) folder, and note that through our [documentation](https://twinlab.ai/) you can find additional example datasets as you get acquainted with using twinLab.
