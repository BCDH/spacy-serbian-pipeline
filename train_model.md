Based on instructions [here](https://spacy.io/usage/training#basics)

1. Clone the repository with the UD data: `git clone https://github.com/BCDH/spacy-serbian-pipeline`
2. make a directory for the converted data: `mkdir sr-data`
3. [Convert](https://nightly.spacy.io/api/cli#convert) the training and dev data: 
   - `python -m spacy convert ./spacy-serbian-pipeline/UD_Serbian_Cyrl-SET/sr_set-ud-train.conllu sr-data`
   - `python -m spacy convert ./spacy-serbian-pipeline/UD_Serbian_Cyrl-SET/sr_set-ud-dev.conllu sr-data`
4. Create a basic [configuration file](https://nightly.spacy.io/api/data-formats#config) using the widget on the [spaCy site](https://nightly.spacy.io/). Copy the text to the clipboard and paste it to a file called `config-basic.cfg`.
5. Fill the basic config file with other spaCy defaults: `python -m spacy init fill-config config-basic.cfg config.cfg`
6. Validate the test and training data (optional, but helpful): `python -m spacy debug data ./config.cfg  --paths.train ./sr-json/sr_set-ud-train.spacy --paths.dev ./sr-json/sr_set-ud-dev.spacy`
7. You can now train the model: `python -m spacy train config.cfg --paths.train ./sr-json/sr_set-ud-train.spacy --paths.dev ./sr-json/sr_set-ud-dev.spacy`

#TODO train model with a custom language object and lookups data 
#TODO learn more about token to vecor layer.  https://nightly.spacy.io/api/cli#pretrain When is this needed? TO what ends? 
