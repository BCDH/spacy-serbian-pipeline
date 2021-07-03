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

doc = nlp('Био је председник владе у том периоду.')

#Jekavian example

#doc = nlp('Овим правилником прописују се захтјеви које у погледу квалитета мора задовољити свјеже сирово млијеко при откупу, начин испитивања његовог квалитета, услови које морају испуњавати лабораторије за испитивање квалитета сировог млијека и критеријуми и начин утврђивања цијене.')


print(f"{'ТОКЕN':<20}{'POS':<8}{'TAG':<15}{'LEMMA':<15}{'NORM':<15}")
print(f"{'¯¯¯¯¯':<20}{'¯¯¯':<8}{'¯¯¯':<15}{'¯¯¯¯¯':<15}{'¯¯¯¯':<15}")

for token in doc:
    print(f"{token.orth_:<20}{token.pos_:<8}{token.tag_:<15}{token.lemma_:<15}{token.norm_:<15}")


#from spacy import displacy
#displacy.serve(doc, style="dep")
#displacy.serve(doc, style="ent") - we don't recognize entities at the moment;
