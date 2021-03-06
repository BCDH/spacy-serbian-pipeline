# -*- coding: utf-8 -*-
#!/usr/local/bin/python3

import spacy

nlp = spacy.load("models/srp/model-best")
#nlp = spacy.load("models/srp/model-last", disable=["ner"]) #we don't actually have a ner model yet

#print("Pipeline:", nlp.pipe_names)

doc = nlp('На отварању БЕМУС-а је требало да учествују нпр. Марта Аргерич и неколико ди-џејева.')

#doc = nlp('На главним вестима ABC-ја гостују нпр. гђа Палавестра и др. На главним вестима Еј-Би-Сија гостује гђа Палавестра. На главним вестима АБЦ-ја гостује гђа Палавестра.')

#Jekavian example

#doc = nlp('Овим правилником прописују се захтјеви које у погледу квалитета мора задовољити свјеже сирово млијеко при откупу, начин испитивања његовог квалитета, услови које морају испуњавати лабораторије за испитивање квалитета сировог млијека и критеријуми и начин утврђивања цијене.')

print(f"{'ТОКЕN':<15}{'NORM':<15}{'LEMMA':<15}{'POS':<8}{'TAG':<15}{'DEP':<8}")
print(f"{'¯¯¯¯¯':<15}{'¯¯¯¯':<15}{'¯¯¯¯¯':<15}{'¯¯¯':<8}{'¯¯¯':<15}{'¯¯¯':<8}")

for token in doc:
    print(f"{token.orth_:<15}{token.norm_:<15}{token.lemma_:<15}{token.pos_:<8}{token.tag_:<15}{token.dep_:<8}")


# for token.pos_ we'll need a tag map
# https://spacy.io/usage/adding-languages#tag-map
# conversion fro UD to json doesn't pick up the POS field if there are more granual tags to deal with_

#from spacy import displacy
#displacy.serve(doc, style="dep")
#displacy.serve(doc, style="ent") - we don't recognize entities at the moment;
