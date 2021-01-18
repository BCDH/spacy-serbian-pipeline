from setuptools import setup

setup(
    name="srp",
    entry_points={
        "spacy_languages": ["srp = srp:SerbianpLanguage"],
    }
)
