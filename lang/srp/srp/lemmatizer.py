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
        # the problem is that Spacy tags Еј-Би-Сија as PUNCT!  

    def __call__(self, doc: Doc) -> Doc:
        for t in doc:
            if t.pos_ in self.non_declinables:
                t.lemma_ = t.text.lower() # for isntance, if a sentence starts with a preposition
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
                #  "мора": {
                #     "NOUN": [
                #         "мора",
                #         "море"
                #     ],
                #     "VERB": "морати"
                # },

                if pos in lemma.keys():
                    if isinstance(lemma[pos], str):
                        return lemma[pos]
                    elif isinstance(lemma[pos], list):
                        return lemma[pos][1] +" !l" # this is random; we would need more info (gender etc. to resolve lists! except for бирократ/а which we may need to turn into one form in json data )
                    else:
                        return "nodict" #at the moment ther are no dicts at this level; we may have them if we decide to further distinguish lists by adding morphosyntactic tagsх
                else:
                    if pos == "AUX":
                        if isinstance(lemma["VERB"], str):
                            return lemma["VERB"]
                        elif isinstance(lemma["VERB"], list):
                            return lemma["VERB"][1] +" !l" #this is random
                        else:
                            return "nodictAtThisLevel AUX"
                    elif (pos == "SCONJ" or pos == "CCONJ"):
                        if isinstance(lemma["CONJ"], str):
                            return lemma["CONK"]
                        elif isinstance(lemma["CONK"], list):
                            return lemma["CONJ"][1] +" !l"#this is random
                        else:
                            return "nodictAtThisLevel CONJ"
                    elif pos == "PROPN":
                        if isinstance(lemma["NOUN"], str):
                            return lemma["NOUN"]
                        elif isinstance(lemma["NOUN"], list):
                            return lemma["NOUN"][1] +" !l"#this is random
                        else:
                            return "nodictAtThisLevel PROPN"
                    elif pos == "DET":
                        if isinstance(lemma["PRON"], str):
                            return lemma["PRON"]
                        elif isinstance(lemma["PRON"], list):
                            return lemma["PRON"][1] +" !l"#this is random
                        else:
                            return "nodictAtThisLevel PRON"
                    else:
                        # here we have tokens that exist in the lookup tables
                        # but not under the pos that spacy assigned to it. for instance if прилично was tagged as a NOUN but it's as ADJ and ADV in the lookups
                        return token + " !mism"
            else:
                # neither string, list or dict, which is impossilbe
                # will get rid of this
                return type(lemma).__name__ +":"+ token
        else:
            #check normalized versions
            lemma = lookup.get(norm, None)
            if isinstance(lemma, str):
                return lemma
            elif isinstance(token, dict):
                return "!normdict"
                #token = list(token.values())[0]
            else:
                return ""
                #return "!" + token
                #token = "!" + token
