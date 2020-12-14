import spacy
nlp = spacy.load("en_core_web_sm")
# print(len(nlp.vocab.lookups.get_table("lemma_lookup")))


doc = nlp('The seat of the UN is in NYC.')


for token in doc:
    token_orth = token.orth_
    token_lemma = token.lemma_
    token_pos = token.pos_
    token_tag = token.tag_
    token_norm = token.norm_
    print(f"{token_orth:<20}{token_pos:<8}{token_tag:<15}{token_lemma:<15}{token_norm:<15}")
