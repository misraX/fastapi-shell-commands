#!/bin/bash

pip3 install virtualenv

virtualenv venv -p python3

source venv/bin/activate

pip install poetry

poetry install


