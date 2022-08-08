# {{ cookiecutter.project_name }}

This repository packages the `{{ cookiecutter.model_class }}` in `{{ cookiecutter.project_slug }}/model.py ` for execution with [Prefect](https://docs.prefect.io/) using the flow described in `{{ cookiecutter.project_slug }}/flow/flow.py`. 


## Installation

This package may be installed using pip:
```
pip install git+{{ cookiecutter.github_url }}
```


## Dev

Create an environment using the environment.yml packaged with the repository:
```
conda env create -f environment.yml
```
Activate your environment:
```
conda activate {{ cookiecutter.project_slug }}
```
Install dev environment:
```
conda env create -f dev-environment.yml
```

Activate your environment:
```
conda activate {{ cookiecutter.project_slug }}-dev
```

Install package:
```
pip install -e .
```

Tests can be executed from the root directory using:
```
pytest .
```

### Note
This README was automatically generated using the template defined in https://github.com/slaclab/lume-services-model-template with the following configuration:

```json
{
    "author": "{{ cookiecutter.author }}",
    "email": "{{ cookiecutter.email }}",
    "github_username": "{{ cookiecutter.github_username }}",
    "github_url": "{{ cookiecutter.github_url }}",
    "project_name": "{{ cookiecutter.project_name }}", 
    "repo_name": "{{ cookiecutter.repo_name }}", 
    "project_slug": "{{ cookiecutter.project_slug }}",
    "model_class": "{{ cookiecutter.model_class }}"
}
```
