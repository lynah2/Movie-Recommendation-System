from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

SRC_REPO = 'src'
LIST_OF_REQUIREMENTS =  ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    description = 'A simple example package for movies recommendation',
    long_description = long_description,
    lont_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS,
)