# CAN_IDS

<p align="left">
  <a href="https://github.com/ZeniteSolar/CAN_IDS/actions?query=workflow:tests">
    <img alt="Test Status" src="https://github.com/ZeniteSolar/CAN_IDS/workflows/tests/badge.svg">
  </a>
</p>

CAN BUS protocol description with code generation for the solar boat modules and applications.

## How it works
  - You programatically describe all modules and its messages using Python language.
  - The script exports a Javascript Object Notation file (.json).  
  - The script exports a documentation (.html). **(not implemented yet)**  
  - The script exports a C header file (.h) with all definitions.  
  - The script exports a Python file (.py) with all encoders and decorders. **(not implemented yet)**  
  - The script exports a JS file (.js) with all encoders and decorders. **(not implemented yet)**  
  - The script exports a C source file (.c) with all encoders and decorders. **(not implemented yet)**  
  - All the files are automatically released in this repository. **(not implemented yet)**  
  - Dependabots automatically detects new versions for your repository. **(not implemented yet)**  
  

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
