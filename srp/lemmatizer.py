# coding: utf8
from __future__ import unicode_literals

from collections import OrderedDict

from spacy.tokens import Doc
import srsly

class SerbianLemmatizer():
    def __init__(self):
        #, lemma_lookup_path, lexeme_norm_lookup_path
        #self.lexeme_norm_lookup = srsly.read_json(lexeme_norm_lookup_path)
        #self.lemma_lookup = srsly.read_json(lemma_lookup_path)
        self.lemma_rules = srsly.read_json('srp_lookups_data/srp_lemma_rules.json')
        self.lemma_lookup =  srsly.read_json('srp_lookups_data/srp_lemma_lookup.json')
        self.non_declinables = ["PUNCT", "ADP", "CCONJ", "SCONJ", "ADV"]
        #lookup_table = self.lookups.get_table("lemma_lookup", {})

    def __call__(self, doc: Doc) -> Doc:
        for t in doc:
            if t.pos_ in self.non_declinables:
                t.lemma_ = t.text
            else:
                t.lemma_ = self.lemmatize(t.text, t.norm_, t.pos_, self.lemma_lookup, self.lemma_rules)
        return doc
    def lemmatize (self, token, norm, pos, lookup, rules):
        # rule-based lemmatization happens first
        for tokenend, lemmaend in rules.items():
            if token.endswith(tokenend):
                lemma = token[: len(token) - len(tokenend)] + lemmaend
                return lemma
        # if no lemma was returned from the rules table, we have to lookup
        lemma = lookup.get(token, None)
        if lemma:
            if isinstance(lemma, str):
                return lemma
            elif isinstance(lemma, list):
                # this will return first element in list
                # this is totally random
                # should be avoided for бирократ/бирократа doubles
                return lemma[0]
            elif isinstance(lemma, dict):
                # dict = two or more key:string or key:list items
                # it's enough to check the first value because
                # it's either or, you can't combine strings and lists
                # "коме": {
                #   "PRON": [
                #    "ко",
                #    "који"
                #   ],
                #   "NOUN": [
                #    "ком",
                #    "кома"
                #   ]
                #  },
                # "Продановим": {
                #     "NOUN": "Проданов",
                #     "ADJ": "Проданов"
                #  },
                if isinstance(next(iter(lemma.values())), str):
                    #return "string"
                    #temp hack b/c of data
                    if pos == "AUX":
                        return lemma["VERB"] or "a"
                    elif (pos == "SCONJ" or pos == "CCONJ"):
                        return lemma["CONJ"] or "b"
                    elif (pos == "PROPN"):
                        return lemma["NOUN"] or "c"
                    elif (pos == "DET"):
                        return lemma["PRON"] or "d"
                    else:
                        return lemma.get(pos, "empty")


                    ## theoretically we could have a pos in the datafile that's NOT matched by the statistical predictionn. what then?
                else:
                    return lemma.get(pos)[1] or "f"

                # if pos in lemma:
                #     return "checkifstr" # lemma[pos] can also be a list!!s
                # #     #return lemma[pos]
                # else:
                #     return "fixthis"


            else:
                return type(lemma).__name__ +":"+ token
                #token = "!" + token
        else:
            #check normalized versions
            lemma = lookup.get(norm, None)
            if isinstance(lemma, str):
                return lemma
            elif isinstance(token, dict):
                return ""
                #token = list(token.values())[0]
            else:
                return "!" + token
                #token = "!" + token
        return token
