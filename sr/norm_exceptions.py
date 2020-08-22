# coding: utf8
from __future__ import unicode_literals

# currently considering for Ekavian-Jekavian normalization

_exc = {
    # jekavian to ekavian
    "млијеко": "млеко",
    "мјесто": "место",
    "мјеста": "места",
    "мијесити": "месити"

}


NORM_EXCEPTIONS = {}

for string, norm in _exc.items():
    NORM_EXCEPTIONS[string] = norm
    NORM_EXCEPTIONS[string.title()] = norm
