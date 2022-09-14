# {{ cookiecutter.project_name }}

This repository packages the `{{ cookiecutter.model_class }}` in `{{ cookiecutter.package }}/model.py ` for execution with [Prefect](https://docs.prefect.io/) using the flow described in `{{ cookiecutter.package }}/flow/flow.py` using the variables:

<!--- The input and output variable tables are replaced when generating the project in template/hooks/post_gen_project.py-->
<<INPUT_VARIABLES>>

<<OUTPUT_VARIABLES>>


## Installation

This package may be installed using pip:
```
pip install git+{{ cookiecutter.github_url }}
```


## Dev

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
    "project_slug": "{{ cookiecutter.project_slug }}", 
    "package": "{{ cookiecutter.package }}",
    "model_class": "{{ cookiecutter.model_class }}"
}
```
