Based on instructions [here](https://spacy.io/usage/training#basics)

1. Clone the repository with the UD data 
2. make a directory for the converted data: `mkdir sr-json`
3. Convert the training and dev data: `python -m spacy convert ./spacy-serbian-pipeline/UD_Serbian_Cyrl-SET/sr_set-ud-train.conllu sr-json`
   - `
