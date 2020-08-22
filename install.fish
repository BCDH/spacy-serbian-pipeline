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


# This won't be of any use for the time being because Serbian UD sets are not Cyrillic.
# We will be training our own dataset.
# # add data for tagger and parser
# git clone https://github.com/UniversalDependencies/UD_Serbian-SET.git
# mkdir serbian-json
# python3 -m spacy convert UD_Serbian-SET/sr_set-ud-train.conllu  serbian-json
# python3 -m spacy convert UD_Serbian-SET/sr_set-ud-dev.conllu  serbian-json
# python3 -m spacy convert UD_Serbian-SET/sr_set-ud-test.conllu  serbian-json
# # train
# mkdir models
# python3 -m spacy train sr models/sr serbian-json/sr_set-ud-train.json serbian-json/sr_set-ud-dev.json -n 1
# # evaluate
# python3 -m spacy evaluate models/sr/model-best serbian-json/sr_set-ud-test.json
