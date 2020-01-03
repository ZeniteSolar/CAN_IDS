# CAN_IDS

<p align="left">
  <a href="https://github.com/ZeniteSolar/CAN_IDS/actions?query=workflow:tests">
    <img alt="Test Status" src="https://github.com/ZeniteSolar/CAN_IDS/workflows/tests/badge.svg">
  </a>
</p>

## Usage
    
Environment setup:

    git clone https://github.com/ZeniteSolar/CAN_IDS
    cd CAN_IDS
    virtualenv env
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

Generating json:

    python can.py
  
Getting the last .json:

    wget https://raw.githubusercontent.com/ZeniteSolar/CAN_IDS/master/can_ids.json

Getting the last .h:

    wget https://raw.githubusercontent.com/ZeniteSolar/CAN_IDS/master/can_ids.h

Running tests:

    sh test.sh
