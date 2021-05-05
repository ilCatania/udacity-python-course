#!/bin/sh
pip install flask -U
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload

