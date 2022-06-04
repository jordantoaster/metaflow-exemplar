#!/bin/bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python src/create_dataset.py
