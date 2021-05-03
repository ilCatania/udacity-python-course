#!/bin/sh
export FLASK_APP=./src/app.py
flask run --host 0.0.0.0 --port 3000 --reload
