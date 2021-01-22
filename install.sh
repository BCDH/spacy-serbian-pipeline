# this is David's attempt at a bash version of my fish install script for spacy 3. it doesn't work. 
rm -rf env
python3 -m venv env
source env/bin/activate
pip install pip setuptools wheel

echo "Install spacy..."
pip install spacy-nightly --pre

echo "Installing lookups data..."

git clone https://github.com/explosion/spacy-lookups-data.git

cp sr_lookups_data/sr_lemma_lookup.json spacy-lookups-data/spacy_lookups_data/data/srp_lemma_lookup.json

cd spacy-lookups-data/
pip install -e .
cd ..

mkdir models
python3 -m spacy init fill-config base_config.cfg config.cfg
python3 -m spacy train config.cfg --output models/srp

# python play3.srp.py
