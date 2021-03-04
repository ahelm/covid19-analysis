# Covid-19 ICU forecast

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ahelm/covid19-icu-forecasting/HEAD)

This repository includes studies done to develop a forecasting model to predict
the number of ICUs based on the development of the COVID-19 numbers. Please
examine the conclusion and the model's extrapolation capabilities mentioned in
the last sections of the notebook.

## Ways to use the notebook

### Binder

Binder makes sharing of notebooks easy. This repo is set up such that it can
utilize Binder directly. Please click
[here to open the notebook in Binder](https://mybinder.org/v2/gh/ahelm/covid19-icu-forecasting/HEAD).

### Local setup

If you wish to use it locally, run the commands below in the shell

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```
