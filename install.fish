#!/usr/local/bin/fish

# -r rebuild spacy from scratch with serbian data + train the model
# -u update serbian data (no model training)
# -t train the model
# -2 use spacy 2.3 build process
# -3 use spacy 3.0 build process: doesn't work in this branch. working on it in a separate brach with the new lemmatizer.

argparse -x 'r,u' -x'2,3' 'r' 'u' 'v' 'd' 'e' '2' '3' 't' -- $argv

if begin; test -z $_flag_u; and test -z $_flag_r; end;
  set _flag_u "-u"
end

if begin; test -z $_flag_2; and test -z $_flag_3; end;
  set _flag_2 "-2"
end

if test $_flag_r
  # rebuild from scratch requires both the data + training the model
  set _flag_t "-t"
  set _flag_u "-u"
end

# check installed version
if test -d env
  source env/bin/activate.fish
  # on Mac we need ggrep (brew install ggrep), the default grep won't do
  switch (uname)
    case Linux
      set installed (pip3 show spacy | grep -oP '(?<=Version:\s)\d')
    case Darwin
      set installed (pip3 show spacy | ggrep -oP '(?<=Version:\s)\d')
  end
else
  set installed 0
end

# Install spacy from scratch
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
  #if rebuilding from scratch, we want to download spacy-lookups-datasets
  if test $_flag_2
    # Clone or pull the spacy lookups data
    if not test -d spacy-lookups-data
      git clone https://github.com/explosion/spacy-lookups-data.git
    else
      cd spacy-lookups-data
      git pull
      cd ..
    end
  else
    # version 3
  end
end

set site (python3 -c "import site; print(site.getsitepackages()[0])")

if test $_flag_u
  # update datasets

  if test $_flag_2
    # Clone or pull the spacy lookups data
    if not test -d spacy-lookups-data
      echo "Cloning spacy lookups data..."
      git clone https://github.com/explosion/spacy-lookups-data.git
    else
      echo "Updating spacy lookup data"
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
    # this next step may take a bit z complete
    pip install -e .
    cd ..
    # Use Serbian pipeline
    echo "Set up Serbian pipeline..."
    python3 setup.py develop
  else
    # no need to do anything here zfor spacy3
  end

end

# git clone https://github.com/UniversalDependencies/UD_Serbian-SET.git
# converted UD datasets to Cyrillic; this is just for starters, we plan to do our own training data
# mkdir training_data
# python3 -m spacy convert UD_Serbian_Cyrl-SET/sr_set-ud-train.conllu  sr_training_data
#python3 -m spacy convert UD_Serbian_Cyrl-SET/sr_set-ud-dev.conllu  sr_training_data
#python3 -m spacy convert UD_Serbian_Cyrl-SET/sr_set-ud-test.conllu  sr_training_data


if test $_flag_t
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
end

echo "Done"

# # evaluate
# python3 -m spacy evaluate models/sr/model-best sr_training_data/sr_set-ud-test.json
