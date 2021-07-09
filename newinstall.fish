#!/usr/bin/env fish


set base_config "base_config"
set lang "srp"
set treebank "UD_Serbian-SET"
set train_name "sr_set-ud-train"
set dev_name "sr_set-ud-dev"
set test_name "sr_set-ud-test"
set package_name "ud_sr_set"
set package_version "0.0.0"
gpu: -1

python3 -m venv env
source env/bin/activate.fish
pip install -U pip setuptools wheel
pip install -U spacy

# Install serbian lang files as package with entry point srp
pip install -e lang/srp/
