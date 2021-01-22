# -*- coding: utf-8 -*-
#!/usr/local/bin/python3
try:
    import sys
    import spacy
except ImportError:
    print("spaCy is probably installed inside a virtual environment. Make sure to activate it.")
    sys.exit()
#print (sys.path)

nlp = spacy.load("models/sr/model-final", disable=["ner"])

doc = nlp('На отварању БЕМУС-а је требало да учествују нпр. Марта Аргерич и неколико ди-џејева.')

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


#from spacy import displacy
#displacy.serve(doc, style="dep")
#displacy.serve(doc, style="ent") - we don't recognize entities at the moment;
