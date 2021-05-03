#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name="meme_generator",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
)
