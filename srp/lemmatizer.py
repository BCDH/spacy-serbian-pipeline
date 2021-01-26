# coding: utf8
from __future__ import unicode_literals

from collections import OrderedDict

from spacy.tokens import Doc
import srsly

class SerbianLemmatizer():
    def __call__(self, doc: Doc) -> Doc:
        lookup = srsly.read_json('srp_lookups_data/srp_lemma_lookup.json')
        for t in doc:
            lemma = lookup.get(t.text, None)
            if lemma:
                t.lemma_ = lemma
        return doc
