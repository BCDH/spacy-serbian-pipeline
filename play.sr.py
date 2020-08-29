import spacy
nlp = spacy.load("models/sr/model-best")
#from spacy.util import get_lang_class
# Serbian = get_lang_class("sr")
# nlp = Serbian()
# print(len(nlp.vocab.lookups.get_table("lemma_lookup")))

doc = nlp('Епидемија коронавируса наметнула је нова правила понашања у школи од 1. септембра, а обавезно ношење маски и физичка дистанца од вршњака, за децу може бити стресно и трауматично, упозоравају стручњаци и истичу да ће важну улогу у прихватању и привикавању малишана на нову реалност имати приступ родитеља и учитеља.')


for token in doc:
    token_text = token.text
    token_lemma = token.lemma_
    token_tag = token.tag_
    token_norm = token.norm_
    print(f"{token_text:<20}{token_tag:<15}{token_lemma:<15}{token_norm:<15}")

# for token.pos_ we'll need a tag map
# https://spacy.io/usage/adding-languages#tag-map
# conversion fro UD to json doesn't pick up the POS field 
