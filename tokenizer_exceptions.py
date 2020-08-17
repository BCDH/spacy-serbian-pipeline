# encoding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH, LEMMA, NORM


# just testing, based on German

# splittting

_exc = {
    "auf'm": [
        {ORTH: "auf", LEMMA: "auf"},
        {ORTH: "'m", LEMMA: "der", NORM: "dem"}
    ],
    "нпр.": [
        {ORTH: "н", LEMMA: "на"},
        {ORTH: "пр", LEMMA: "пример", NORM: "пример"}
    ]

}

# grouping

for exc_data in [
    {ORTH: "usw.", LEMMA: "und so weiter"},
    {ORTH: "итд.", LEMMA: "и тако даље"},
]:
    _exc[exc_data[ORTH]] = [exc_data]


# check later if those exist in German look up tables as such?

for orth in [
    "vs.",
    "wiss."
]:
    _exc[orth] = [{ORTH: orth}]


TOKENIZER_EXCEPTIONS = _exc
