# coding: utf8
from __future__ import unicode_literals

from collections import OrderedDict

from spacy.tokens import Doc
import srsly

class SerbianLemmatizer():
    def __call__(self, doc: Doc) -> Doc:
        lookup = srsly.read_json('srp_lookups_data/srp_lemma_lookup.json')

        for t in doc:
            t.lemma_ = self.lemmatize(t.text, t.norm_, t.pos_, lookup)
        return doc
    def lemmatize (self, candidate, norm, pos, lookup):
        lemma = lookup.get(candidate, None)
        if lemma:
            if isinstance(lemma, str):
                return lemma
            elif isinstance(lemma, list):
                # this will return first element in list
                # this is totally random
                # should be avoided for бирократ/бирократа doubles
                return lemma[0]
            elif isinstance(lemma, dict):
                # temp hack b/c of data
                if pos == "AUX":
                    return lemma["VERB"]
                elif (pos == "SCONJ" or pos == "CCONJ"):
                    return lemma["CONJ"]
                elif (pos == "PROPN"):
                    return lemma["NOUN"]
                else:
                    return lemma[pos]



            else:
                return type(lemma).__name__ +":"+ candidate
                #candidate = "!" + candidate
        else:
            #check normalized versions
            lemma = lookup.get(norm, None)
            if isinstance(lemma, str):
                return lemma
            elif isinstance(candidate, dict):
                return ""
                #candidate = list(candidate.values())[0]
            else:
                return "!" + candidate
                #candidate = "!" + candidate
        return candidate
