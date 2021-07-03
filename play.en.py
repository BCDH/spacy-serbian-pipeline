import spacy
nlp = spacy.load("en_core_web_sm")


doc = nlp('He eats, shoots and leaves.')

print(f"{'ТОКЕN':<15}{'POS':<8}{'TAG':<8}{'LEMMA':<15}{'NORM':<15}")
print(f"{'¯¯¯¯¯':<15}{'¯¯¯':<8}{'¯¯¯':<8}{'¯¯¯¯¯':<15}{'¯¯¯¯':<15}")

for token in doc:
    print(f"{token.orth_:<15}{token.pos_:<8}{token.tag_:<8}{token.lemma_:<15}{token.norm_:<15}")

from spacy import displacy
displacy.serve(doc, style="dep")
