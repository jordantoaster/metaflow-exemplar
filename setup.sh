#!/bin/bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt

mkdir ~/.metaflowconfig/
cp config/config.json ~/.metaflowconfig/

python src/create_dataset.py


