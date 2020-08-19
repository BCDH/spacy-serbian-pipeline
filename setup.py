from setuptools import setup

setup(
    name="srx",
    entry_points={
        "spacy_languages": ["srx = srx:SerbianLanguage"],
    }
)