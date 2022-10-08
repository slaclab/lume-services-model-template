# LUME-services Model Template
This repository provides a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) model template for compatibility with [LUME-services](https://slaclab.github.io/lume-services/) orchestration tooling.


## Tools
* conda
* click for cli dev
* versioneer (cookiecutter runs install during post-installation hook)
* pytest with coverage
* Common github actions
* [pydantic](https://pydantic-docs.helpmanual.io/) for use with data structures

## Demo
[Demo](https://slaclab.github.io/lume-services/demo/)

### Notes
 - Jinja templating with GitHub actions requires raw blurbs

Conda vs pip installation
- runtime requirement should make an effor to only reference conda-forge distributions and include requirements as conda distributions for those necessarily installed with pip


