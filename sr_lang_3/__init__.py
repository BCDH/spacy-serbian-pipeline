# coding: utf8
from __future__ import unicode_literals

from .stop_words import STOP_WORDS
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
#from .norm_exceptions import NORM_EXCEPTIONS
from .tag_map import TAG_MAP
from .lex_attrs import LEX_ATTRS
from spacy.language import Language
from spacy.lang.tokenizer_exceptions import BASE_EXCEPTIONS
from spacy.lang.norm_exceptions import BASE_NORMS
from spacy.lookups import Lookups
from spacy.attrs import LANG, NORM
from spacy.util import update_exc, add_lookups


class SerbianDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters.update(LEX_ATTRS)
    lex_attr_getters[LANG] = lambda text: "sr"
    # the following bit was giving me errors when building under 3.0
    #lex_attr_getters[NORM] = add_lookups(
    #    Language.Defaults.lex_attr_getters[NORM], BASE_NORMS, NORM_EXCEPTIONS
    #)
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    stop_words = STOP_WORDS
    tag_map = TAG_MAP


class SerbianLanguage(Language):
    lang = "sr"
    Defaults = SerbianDefaults


__all__ = ["SerbianLanguage"]
