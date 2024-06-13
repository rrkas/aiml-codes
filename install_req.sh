#!/bin/bash

# the script will terminate as soon as any command inside it fails
set -e

pip install ./subjects/NLP/en_core_web_sm-3.7.1-py3-none-any.whl
pip install -U -r ./requirements.txt
pip-chill --no-version > ./requirements.txt

echo "DONE!"
