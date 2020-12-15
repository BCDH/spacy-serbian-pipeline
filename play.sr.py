# -*- coding: utf-8 -*-
#!/usr/local/bin/python3

import spacy
nlp = spacy.load("models/sr/model-best", disable=["ner"])
#from spacy.util import get_lang_class
# Serbian = get_lang_class("sr")
# nlp = Serbian()
# print(len(nlp.vocab.lookups.get_table("lemma_lookup")))

doc = nlp('Професор на Универзитету „Џонс Хопкинс” у Вашингтону Данијел Сервер изјавио је да ће некадашња шефица америчке дипломатије Медлин Олбрајт бити укључена у дијалог Београда и Приштине у име наредне администрације САД, без обзира на то шта Срби мисле о њој. „Није важно шта Срби мисле о томе да Медлин Олбрајт буде укључена или не. Она ће бити укључена. Бивша је државна секретарка и важна је струја, не толико у Демократској странци, већ у мислећем демократском свету, делу демократског света који мисли о спољног политици. А и живела је у Србији, говори српски. Мислим да би то требало ценити”, рекао је Сервер за телевизију Н1, пренео је Танјуг. Сервер је казао да разуме да је „многи Срби неће ценити јер је заговарала учешће НАТО у рату после пропасти преговора у Рамбујеу”.')

# doc = nlp('На отварању БЕМУС-а је требало да учествују нпр. Марта Аргерич и неколико ди-џејева.')

#doc = nlp('На главним вестима ABC-ја гостују нпр. гђа Палавестра и др. На главним вестима Еј-Би-Сија гостује гђа Палавестра. На главним вестима АБЦ-ја гостује гђа Палавестра.')

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
