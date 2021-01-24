# -*- coding: utf-8 -*-
#!/usr/local/bin/python3

import spacy

nlp = spacy.load("models/srp/model-last", disable=["ner"])
#nlp.add_pipe("lemmatizer", config={"mode": "lookup"})
#nlp.initialize()

#print(lemmatizer.mode)  # 'rule'

#print (nlp.tokenizer.vocab.lookups.get_table('lemma_lookup').get('пије'))

#from spacy.util import get_lang_class
#Serbian = get_lang_class("sr")
#nlp = Serbian()
#print(len(nlp.vocab.lookups.get_table("lemma_lookup")))

doc = nlp('На отварању БЕМУС-а је требало да учествују нпр. Марта Аргерич и неколико ди-џејева.')

#doc = nlp('На главним вестима ABC-ја гостују нпр. гђа Палавестра и др. На главним вестима Еј-Би-Сија гостује гђа Палавестра. На главним вестима АБЦ-ја гостује гђа Палавестра.')

#Jekavian example

#doc = nlp('Овим правилником прописују се захтјеви које у погледу квалитета мора задовољити свјеже сирово млијеко при откупу, начин испитивања његовог квалитета, услови које морају испуњавати лабораторије за испитивање квалитета сировог млијека и критеријуми и начин утврђивања цијене.')

print(f"{'ТОКЕN':<20}{'POS':<8}{'TAG':<15}{'LEMMA':<15}{'NORM':<15}")
print(f"{'¯¯¯¯¯':<20}{'¯¯¯':<8}{'¯¯¯':<15}{'¯¯¯¯¯':<15}{'¯¯¯¯':<15}")

for token in doc:
    token_orth = token.orth_
    token_lemma = token.lemma_
    token_pos = token.pos_
    token_tag = token.tag_
    token_norm = token.norm_
    print(f"{token_orth:<20}{token_pos:<8}{token_tag:<15}{token_lemma:<15}{token_norm:<15}")

# for token.pos_ we'll need a tag map
# https://spacy.io/usage/adding-languages#tag-map
# conversion fro UD to json doesn't pick up the POS field if there are more granual tags to deal with

#from spacy import displacy
#displacy.serve(doc, style="dep")
#displacy.serve(doc, style="ent") - we don't recognize entities at the moment;
