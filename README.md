# Serbian Language Pipeline for Spacy

We're just starting with this project.

## How to use with Spacy?

...

## Data files

At the moment, the UD dataset which has been automatically converted to Cyrillic. This is temporary, while we're setting up our workflow. 

### Lemmatizer data

- `sr_lemma_lookup.json`
- data originates from Morpho-SLaWS (Tasovac, Rudan and Rudan 2015) and Transpoetika (Tasovac 2012)
- currently includes no polylexical items or personal names, still have to decide on how I will deal with them
- currently includes both Ekavian and Jekavian forms, I may move Jekavians to the normalization function
