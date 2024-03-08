#!/bin/bash

# Update project
git pull

# Check if the virtual environment exists
if [ -d "venv" ]
then
    echo "Virtual environment exists. Starting..."
    source venv/bin/activate
else
    echo "Virtual environment does not exist. Creating..."
    python3 -m venv venv
    source venv/bin/activate
    # You can add any additional setup steps here if needed
fi

# install all requirements
pip install -r requirements.txt

# start the process
# Start a screen session named "roles_bot"
screen -S roles_bot -d -m bash -c 'streamlit run roles_bot.py'

# Close the screen in the background
screen -S roles_bot -X quit