# coding: utf8
from __future__ import unicode_literals
from typing import Optional
from thinc.api import Model

from .lemmatizer import SerbianLemmatizer
from .stop_words import STOP_WORDS
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .lex_attrs import LEX_ATTRS
from spacy.lang.tokenizer_exceptions import BASE_EXCEPTIONS
#from .morph_rules import MORPH_RULES # if we ever start using them

from spacy.language import Language
from spacy.attrs import LANG
from spacy.util import update_exc
from spacy.lookups import Lookups

from spacy.tokens import Doc
import srsly

class SerbianDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters.update(LEX_ATTRS)
    lex_attr_getters[LANG] = lambda text: "srp"
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    stop_words = STOP_WORDS
    #morph_rules = MORPH_RULES #if we ever start using them

class SerbianLanguage(Language):
    lang = "srp"
    Defaults = SerbianDefaults

@Language.factory(
    "srp_lemmatizer",
    assigns=["token.lemma"],
    default_config={"model":None, "mode":"lookup", "overwrite": False},
    default_score_weights={"lemma_acc": 1.0},
)
def make_lemmatizer(
    nlp: Language,
    model: Optional[Model],
    name: str,
    mode: str,
    overwrite: bool = False,
):
    return SerbianLemmatizer()


__all__ = ["SerbianLanguage", "make_lemmatizer"]
