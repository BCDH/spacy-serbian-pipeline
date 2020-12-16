Based on instructions [here](https://spacy.io/usage/training#basics)

1. Clone the repository with the UD data: `git clone https://github.com/BCDH/spacy-serbian-pipeline`
2. make a directory for the converted data and trained models: `mkdir sr-data` && `mkdir models`
3. [Convert](https://nightly.spacy.io/api/cli#convert) the training and dev data:
   - `python -m spacy convert ./spacy-serbian-pipeline/UD_Serbian_Cyrl-SET/sr_set-ud-train.conllu sr-data`
   - `python -m spacy convert ./spacy-serbian-pipeline/UD_Serbian_Cyrl-SET/sr_set-ud-dev.conllu sr-data`
4. Create a basic [configuration file](https://nightly.spacy.io/api/data-formats#config) using the widget on the [spaCy site](https://nightly.spacy.io/). Copy the text to the clipboard and paste it to a file called `config-basic.cfg`.
5. Fill the basic config file with other spaCy defaults: `python -m spacy init fill-config config-basic.cfg config.cfg`
6. Validate the test and training data (optional, but helpful): `python -m spacy debug data ./config.cfg  --paths.train ./sr-json/sr_set-ud-train.spacy --paths.dev ./sr-json/sr_set-ud-dev.spacy`
7. You can now train the model: `python -m spacy train config.cfg --output models --paths.train ./sr-json/sr_set-ud-train.spacy --paths.dev ./sr-json/sr_set-ud-dev.spacy`

#TODO train model with a custom language object and lookups data

## Issues

- when using the config file to train a language model, I can't do it with `__init__.py` in the `sr` directory because of the changes from 2.3 to 3.0
- I can train under 3.0 by replacing `__init__.py` in the `sr` directory with `__init__.py` from `sr_lang_3` and by replacing `tokenizer_exceptions.py` in `sr` with `tokenizer_exceptions.py` from `sr_lang_3`
- HOWEVER, after training by running `python3 -m spacy train config.cfg --output models/sr`(`config.cfg` is an expanded version of `base_config.cfg`), I get a model that can tag text, but not lemmatize or normalize, because our config file didn't pick up the lookups data
- I can't figure out how to add lookups to the config file. I tried adding `lookups = "sr_lookups_data/sr_lemma_lookup.js"` under `[initialize] ` in the base config file, but this gives me an error: `initialize -> lookups   instance of Lookups expected`


#TODO learn more about token to vecor layer.  
https://nightly.spacy.io/api/cli#pretrain

When is this needed? TO what ends?
