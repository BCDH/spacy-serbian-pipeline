from setuptools import setup

setup(
    name="sr",
    entry_points={
        "spacy_languages": ["sr = sr:SerbianLanguage"],
    }
)