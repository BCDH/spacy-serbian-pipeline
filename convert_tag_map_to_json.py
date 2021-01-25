import spacy
import srsly

# this works in v2.3
# used to convert the the new tag_map json format

nlp = spacy.load("models/sr/model-final")
tag_map = {}

# convert any integer IDs to strings for JSON
for tag, morph in nlp.vocab.morphology.tag_map.items():
    tag_map[tag] = {}
    for feat, val in morph.items():
        feat = nlp.vocab.strings.as_string(feat)
        if not isinstance(val, bool):
            val = nlp.vocab.strings.as_string(val)
        tag_map[tag][feat] = val

srsly.write_json("tag_map.json", tag_map)
