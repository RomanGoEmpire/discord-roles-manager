#!/bin/bash

screen -dmS roles_bot bash -c "
git pull;
if [ ! -d 'venv' ]; then
    python3 -m venv venv;
fi
source venv/bin/activate;
pip install -r requirements.txt;
streamlit run your_app.py;
bash
"