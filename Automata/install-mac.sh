#!/bin/bash
pip3 install -r requirements.txt
virtualenv venv
source venv/bin/activate
python3 automata.py
deactivate

