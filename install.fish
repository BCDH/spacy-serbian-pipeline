#!/usr/local/bin/fish

# -r rebuild spacy from scratch
# -u update serbian model only
# -2 use spacy 2.3 build process
# -3 use spacy 3.0 build process
#
# training model under 3.0 gives me an error because of the config file
# needs a fix 

argparse -x 'r,u' -x'2,3' 'r' 'u' 'v' '2' '3' -- $argv

if begin; test -z $_flag_u; and test -z $_flag_r; end;
  set _flag_u "-u"
end

if begin; test -z $_flag_2; and test -z $_flag_3; end;
  set _flag_2 "-2"
end

if test $_flag_r
  if test -d env
    echo "Removing previous installation..."
    rm -rf env
  end
end


if test -d env
  echo "Virtual environment is already installed."
else
  python3 -m venv env
  source env/bin/activate.fish
  pip install -U pip setuptools wheel
  if test $_flag_2
    pip install -U spacy #this still installs version spacy 2.3
  else
    pip install -U spacy-nightly[transformers] --pre
  end
  python3 -m spacy download en_core_web_sm
  python3 -m spacy download de_core_news_sm
end


# Get spacy lookups data
if command git clone https://github.com/explosion/spacy-lookups-data.git
else
    cd spacy-lookups-data
    git pull
    cd ..
end

# Use our lookups instead the default one
echo "Copying local sr_lemma_lookup.json to the spacy lookup data..."
cp sr/sr_lemma_lookup.json spacy-lookups-data/spacy_lookups_data/data/sr_lemma_lookup.json
cd spacy-lookups-data/
echo "Installing lookup data..."
# this next step may take a bit to complete
pip3 install -e .
cd ..

# Use Serbian pipeline
echo "Set up Serbian pipeline..."
python3 setup.py develop

# add data for tagger and parser
# git clone https://github.com/UniversalDependencies/UD_Serbian-SET.git
# converted UD datasets to Cyrillic; this is just for starters, we plan to do our own training data
# mkdir training_data
# python3 -m spacy convert UD_Serbian_Cyrl-SET/sr_set-ud-train.conllu  sr_training_data
#python3 -m spacy convert UD_Serbian_Cyrl-SET/sr_set-ud-dev.conllu  sr_training_data
#python3 -m spacy convert UD_Serbian_Cyrl-SET/sr_set-ud-test.conllu  sr_training_data
# # train
rm -rf models; and mkdir models
echo "Train model... "
if test $_flag_2
  python3 -m spacy train sr models/sr sr_training_data/sr_set-ud-train.json sr_training_data/sr_set-ud-dev.json -n 1 -V 0.0.1
else
  python3 -m spacy train base_config.cfg --output models/sr
end

# # evaluate
# python3 -m spacy evaluate models/sr/model-best sr_training_data/sr_set-ud-test.json
