#!/usr/bin/env fish

rm -rf env
python3 -m venv env
source env/bin/activate.fish
pip install -U pip setuptools wheel
# no transformers
pip install -U spacy[lookups]


# Install serbian lang files as package with entry point srp
pip install -e lang/srp/

# Convert corpora
# python3 -m spacy convert lang/assets/corpus/UD_Serbian_SET/sr_set-ud-train.conllu lang/assets/corpus/UD_Serbian_SET/ --converter conllu --n-sents 10 --merge-subtokens
# python3 -m spacy convert lang/assets/corpus/UD_Serbian_SET/sr_set-ud-dev.conllu lang/assets/corpus/UD_Serbian_SET/ --converter conllu --n-sents 10 --merge-subtokens
# python3 -m spacy convert lang/assets/corpus/UD_Serbian_SET/sr_set-ud-test.conllu lang/assets/corpus/UD_Serbian_SET/ --converter conllu --n-sents 10 --merge-subtokens
# mv lang/assets/corpus/UD_Serbian_SET/sr_set-ud-train.spacy lang/assets/corpus/UD_Serbian_SET/train.spacy
# mv lang/assets/corpus/UD_Serbian_SET/sr_set-ud-dev.spacy lang/assets/corpus/UD_Serbian_SET/dev.spacy
# mv lang/assets/corpus/UD_Serbian_SET/sr_set-ud-test.spacy lang/assets/corpus/UD_Serbian_SET/test.spacy

# Configure
spacy init fill-config configs/base_config.cfg configs/config.cfg
#
#DDebug
spacy debug config configs/config.cfg
spacy debug data configs/config.cfg

spacy train configs/config.cfg --output training
