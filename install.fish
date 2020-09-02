# Install spacy in a virtual environtment

#python3 -m venv env
#source env/bin/activate.fish
#pip3 install --upgrade pip
#pip3 install -U spacy
#python3 -m spacy download en_core_web_sm
#python3 -m spacy download de_core_news_sm

# Get spacy lookups data

if command git clone https://github.com/explosion/spacy-lookups-data.git
else
    cd spacy-lookups-data
    git pull
    cd ..
end

# Use our lookups instead the default one
cp sr/sr_lemma_lookup.json spacy-lookups-data/spacy_lookups_data/data/sr_lemma_lookup.json
cd spacy-lookups-data/
# this next step may take a bit to complete
pip3 install -e .
cd ..

# Use Serbian pipeline
python3 setup.py develop

# add data for tagger and parser
# git clone https://github.com/UniversalDependencies/UD_Serbian-SET.git
# converted UD datasets to Cyrillic; this is just for starters, we plan to do our own training data
# mkdir training_data
# python3 -m spacy convert UD_Serbian_Cyrl-SET/sr_set-ud-train.conllu  sr_training_data
#python3 -m spacy convert UD_Serbian_Cyrl-SET/sr_set-ud-dev.conllu  sr_training_data
#python3 -m spacy convert UD_Serbian_Cyrl-SET/sr_set-ud-test.conllu  sr_training_data
# # train
rm -rf models
mkdir models
python3 -m spacy train sr models/sr sr_training_data/sr_set-ud-train.json sr_training_data/sr_set-ud-dev.json -n 1 --version 0.0.1
# # evaluate
# python3 -m spacy evaluate models/sr/model-best sr_training_data/sr_set-ud-test.json
