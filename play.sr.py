from spacy.util import get_lang_class
Serbian = get_lang_class("sr")
nlp = Serbian()
# print(len(nlp.vocab.lookups.get_table("lemma_lookup")))


doc = nlp('Шта се дешава са скраћеницама типа нпр. БЕМУС-а? Из ког мјеста долазиш?')


for token in doc:
    token_text = token.text
    token_lemma = token.lemma_
    token_pos = token.pos_
    token_norm = token.norm_
    print(f"{token_text:<20}{token_pos:<15}{token_lemma:<15}{token_norm:<15}")
