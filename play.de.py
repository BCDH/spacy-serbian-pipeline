import spacy
nlp = spacy.load("de_core_news_sm")
# print(len(nlp.vocab.lookups.get_table("lemma_lookup")))


doc = nlp('wiss. Mitarbeiterin.')


for token in doc:
    token_text = token.text
    token_lemma = token.lemma_
    #token_dep = token.dep_
    print(f"{token_text:<20}{token_lemma:<10}")
