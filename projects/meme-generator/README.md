[![Build](https://github.com/ilCatania/udacity-python-course/actions/workflows/meme-generator.yml/badge.svg)](https://github.com/ilCatania/udacity-python-course/actions/workflows/meme-generator.yml)
[![codecov](https://codecov.io/gh/ilCatania/udacity-python-course/branch/master/graph/badge.svg?token=6M9ZFBRIF2)](https://codecov.io/gh/ilCatania/udacity-python-course)

Meme Generator project
======================

This is a collection of utilities to generate
meme-like pictures from collections of quotes
and pictures.

## How to build
To build the project, you will first need to have
Python installed. This was developed against Python
version `3.8.5`. You will also need `pip` and,
optionally, `virtualenv`.

All the commands in the below listings will be
assumed to be running in the same directory where
you found this `README`, unless otherwise specified.
I will also assume you are developing under Linux (I
used Ubuntu).

### Set up a virtual environment (optional - recommended)

```sh
$ python -m venv env
$ source env/bin/activate
```

### Code and docstring linting
```sh
$ pip install flake8 flake8-docstrings
$ flake8
```

### Download dependencies and run tests
```sh
$ pip install -r requirements.txt
$ pytest
```

