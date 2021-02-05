#!/usr/local/bin/fish

# -r rebuild spacy from scratch
# -u update serbian model only NOT YET
# -2 use spacy 2.3 build process
# -3 use spacy 3.0 build process: doesn't work in this branch. working on it in a separate brach with the new lemmatizer. 

argparse -x 'r,u' -x'2,3' 'r' 'u' 'v' 'd' 'e' '2' '3' -- $argv

if begin; test -z $_flag_u; and test -z $_flag_r; end;
  set _flag_u "-u"
end

if begin; test -z $_flag_2; and test -z $_flag_3; end;
  set _flag_2 "-2"
end

# Install spacy from scratch
# TODO: add a test so that you can't -u3 if the installed spacy is v2 and vice versa

if test $_flag_r
  if test -d env
    echo "Removing previous installation..."
    rm -rf env
  end
  python3 -m venv env
  source env/bin/activate.fish
  pip install -U pip setuptools wheel
  if test $_flag_2
    pip install -U spacy==2.3.5
  else
    echo "Installing spacy-nightly"
    pip install -U spacy
    #[transformers,lookups]
  end
  # install english and german models if using -e and -dflags
  if test $_flag_d
    python3 -m spacy download de_core_news_sm
  end
  if test $_flag_e
    python3 -m spacy download en_core_web_sm
  end
end

set site (python3 -c "import site; print(site.getsitepackages()[0])")

if test $_flag_2
  # not doing any symlinking anymore
  # keeping spacy 2 stuff in sr
  # and spacy 3 is in srp etc.
  # Clone or pull the spacy lookups data
  if command git clone https://github.com/explosion/spacy-lookups-data.git
  else
      cd spacy-lookups-data
      git pull
      cd ..
  end
  echo "Copying local sr_lemma_lookup.json to the spacy lookup data..."
  # make sure you generate SLAWS normalization files to
  # sr_lookups_data/sr_lexeme_norm.json once we move to spacy3
  cp sr_lookups_data/sr_lemma_lookup.json spacy-lookups-data/spacy_lookups_data/data/sr_lemma_lookup.json
  cp sr_lookups_data/sr_lexeme_norm.json spacy-lookups-data/spacy_lookups_data/data/sr_lexeme_norm.json
  cd spacy-lookups-data/
  echo "Installing lookups data..."
  # this next step may take a bit to complete
  pip install -e .
  cd ..
  # Use Serbian pipeline
  echo "Set up Serbian pipeline..."
  python3 setup.py develop

else
  # no need to do anything here for spacy3
end

# git clone https://github.com/UniversalDependencies/UD_Serbian-SET.git
# converted UD datasets to Cyrillic; this is just for starters, we plan to do our own training data
# mkdir training_data
# python3 -m spacy convert UD_Serbian_Cyrl-SET/sr_set-ud-train.conllu  sr_training_data
#python3 -m spacy convert UD_Serbian_Cyrl-SET/sr_set-ud-dev.conllu  sr_training_data
#python3 -m spacy convert UD_Serbian_Cyrl-SET/sr_set-ud-test.conllu  sr_training_data


if not test -d models
    mkdir models
else
  rm -rf models
  mkdir models
end

echo "Train model... "
if test $_flag_2
  python3 -m spacy train sr models/sr sr_training_data/sr_set-ud-train.json sr_training_data/sr_set-ud-dev.json -n 1 -V 0.0.1
else
  python3 -m spacy init fill-config base_config.cfg config.cfg
  python3 -m spacy train config.cfg --output models/srp
  #python3 -m spacy ray train config.cfg --output models/srp --n-workers 2
end


# move back version 2 files
# if test $_flag_3
#   #mv sr/__init__.py.bak sr/__init__.py; and mv sr/tokenizer_exceptions.py.bak sr/tokenizer_exceptions.py
# end

# remove symlinks
#cd sr
#echo "Deleting symbolic links from sr"
#find . -maxdepth 1 -type l -ls -delete > /dev/null

# # evaluate
# python3 -m spacy evaluate models/sr/model-best sr_training_data/sr_set-ud-test.json
