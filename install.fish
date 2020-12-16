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
end




# Clone or pull the spacy lookups data
if command git clone https://github.com/explosion/spacy-lookups-data.git
else
    cd spacy-lookups-data
    git pull
    cd ..
end

# Use our lookups instead the default one
echo "Copying local sr_lemma_lookup.json to the spacy lookup data..."
cp sr_lookups_data/sr_lemma_lookup.json spacy-lookups-data/spacy_lookups_data/data/sr_lemma_lookup.json
cd spacy-lookups-data/
echo "Installing lookups data..."
# this next step may take a bit to complete
pip3 install -e .
cd ..

# language data are different under 2 and 3
# im doing this hacky nonsense because for the time being, i have to use both 2.3 and 3.0
if test $_flag_3
  mv sr/__init__.py sr/__init__.py.bak; and cp sr_lang_3/__init__.py sr/__init__.py; and mv sr/tokenizer_exceptions.py sr/tokenizer_exceptions.py.bak; and cp sr_lang_3/tokenizer_exceptions.py sr/tokenizer_exceptions.py
end

# Use Serbian pipeline
echo "Set up Serbian pipeline..."
python3 setup.py develop

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
  python3 -m spacy init fill-config base_config.cfg config.cfg
  python3 -m spacy train config.cfg --output models/sr
end


# move back version 2 files
if test $_flag_3
  mv sr/__init__.py.bak sr/__init__.py; and mv sr/tokenizer_exceptions.py.bak sr/tokenizer_exceptions.py
end

# # evaluate
# python3 -m spacy evaluate models/sr/model-best sr_training_data/sr_set-ud-test.json
