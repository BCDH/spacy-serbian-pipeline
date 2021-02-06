import spacy

nlp = spacy.load("training/model-best")

doc = nlp('На отварању БЕМУС-а је требало да учествују нпр. Марта Аргерич и неколико ди-џејева.')

print(f"{'ТОКЕN':<20}{'POS':<8}{'TAG':<15}{'LEMMA':<15}{'NORM':<15}")
print(f"{'¯¯¯¯¯':<20}{'¯¯¯':<8}{'¯¯¯':<15}{'¯¯¯¯¯':<15}{'¯¯¯¯':<15}")

for token in doc:
    token_orth = token.orth_
    token_lemma = token.lemma_
    token_pos = token.pos_
    token_tag = token.tag_
    token_norm = token.norm_
    print(f"{token_orth:<20}{token_pos:<8}{token_tag:<15}{token_lemma:<15}{token_norm:<15}")
