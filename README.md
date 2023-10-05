# twinLab-Demos

<p align="center">
    <!-- <img src="./resources/images/logo.svg" width="200" height="200" /> -->
    <img src="./resources/images/twinLab.svg" width="200" height="200"/>
</p>

![digiLab](./resources/images/digiLab_badge.svg)
![twinLab](./resources/images/twinLab_badge.svg)
[![slack](https://img.shields.io/badge/slack-@digilabglobal-purple.svg?logo=slack)](https://digilabglobal.slack.com)

## Quick Start

Clone the repository and change directory to the project root:
```shell
git clone https://github.com/digiLab-ai/twinLab-Demos.git
cd twinLab-Demos
```

Install the dependencies:
```shell
poetry install
```

Copy the `.env.example` file to `.env` 
```shell
cp .env.example .env
```
and fill out your `twinLab` login details in `.env`

Run the notebook you would like to see, e.g [01-basic notebook](./01-basic.ipynb):
```shell
poetry run jupyter notebook 01-basic.ipynb
```