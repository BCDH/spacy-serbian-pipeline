# coding: utf8
from __future__ import unicode_literals

from .stop_words import STOP_WORDS
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
#from .norm_exceptions import NORM_EXCEPTIONS
#from .tag_map import TAG_MAP
from .lex_attrs import LEX_ATTRS
from spacy.language import Language
from spacy.lang.tokenizer_exceptions import BASE_EXCEPTIONS
from spacy.lang.norm_exceptions import BASE_NORMS
from spacy.lookups import Lookups
from spacy.attrs import LANG, NORM
from spacy.util import update_exc, add_lookups
from spacy.tokens import Doc

import srsly

class SerbianpDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters.update(LEX_ATTRS)
    lex_attr_getters[LANG] = lambda text: "srp"
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    stop_words = STOP_WORDS
    #tag_map = TAG_MAP


class SerbianpLanguage(Language):
    lang = "srp"
    Defaults = SerbianpDefaults


class SerbianpLemmatizer:
    def __call__(self, doc: Doc) -> Doc:
        lookup = srsly.read_json('srp_lookups_data/srp_lemma_lookup.json')
        for t in doc:
            lemma = lookup.get(t.text, None)
            if lemma:
                t.lemma_ = lemma
        return doc


@Language.factory(
    "srp_lemmatizer",
    assigns=["token.lemma"],
    default_config={},
    default_score_weights={"lemma_acc": 1.0},
)
def make_lemmatizer(
    nlp: Language,
    name: str,
):
    return SerbianpLemmatizer()


__all__ = ["SerbianpLanguage", "make_lemmatizer"]
