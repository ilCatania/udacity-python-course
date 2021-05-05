#!/bin/sh
which python
apt-get install python3-venv
python3 -m venv env
source env/bin/activate
pip install numpy
deactivate
pip freeze
pip freeze > requirements.txt
pip install -r requirements.txt

