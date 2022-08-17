# LUME-services Model Template
This repository provides a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) model template for compatibility with [LUME-services](https://slaclab.github.io/lume-services/) orchestration tooling.


## Tools
* conda
* click for cli dev
* versioneer (cookiecutter runs install during post-installation hook)
* [pre-commit](https://pre-commit.com/) hook with black and flake8
* pytest with coverage
* Common github actions
* [pydantic](https://pydantic-docs.helpmanual.io/) for use with data structures

## Demo
[Demo](https://raw.githubusercontent.com/jacquelinegarrahan/lume-services/main/docs/demo.md)

### Notes
 - Jinja templating and github actions

Conda vs pip installation
- runtime requirement should make an effor to only reference conda-forge distributions


