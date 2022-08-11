# LUME-services Model Template
This repository provides a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) model template for compatibility with [LUME-services](https://slaclab.github.io/lume-services/) orchestration tooling.


## Use
1. Create a configuration file describing the input/output variables of your model. https://slaclab.github.io/lume-model/#configuration-files

2. Create a .json file with the following format:
```json
{
    "author": "Jacqueline Garrahan",
    "email": "jacquelinegarrahan@gmail.com",
    "github_username": "jacquelinegarrahan",
    "github_url": "https://github.com/jacquelinegarrahan/test_project.git",
    "project_name": "My Package", 
    "repo_name": "{{ cookiecutter.project_name.lower().replace(' ', '-') }}", 
    "project_slug": "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}",
    "model_class":"{{ cookiecutter.project_name.title().replace(' ', '').replace('-', '') }}"
}
```
For repo_name, project_slug, and model class, we here convert the project name into a palatable form, subbing underscores for dashes and spaces. Alternatively, you may hard-code these values.  


3. Build template (from this repo root)
```
cookiecutter /template -o my_project_name 
```

The template copies your variable configuration to the new project repository and into a subdirectory created using the project slug specified in your .json file. 

The templating workflow also initialized a git repository for your project and creates an initial commit. You can integrate this with a GitHub repository following the instructions outlined [here](https://gist.github.com/alexpchin/102854243cd066f8b88e).


3. Edit the code in my_project_name/ to create a model class representative of your workflow

4. Update your flow in my_project_name/flow

## Use 

Create a .json file:
```
{
    "author": "Jacqueline Garrahan",
    "email": "jacquelinegarrahan@gmail.com",
    "github_username": "jacquelinegarrahan",
    "github_url": "https://github.com/jacquelinegarrahan/test_cookiecutter_project.git",
    "project_name": "My Package", 
    "repo_name": "{{ cookiecutter.project_name.lower().replace(' ', '-') }}", 
    "project_slug": "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}",
}
```




## Tools
* conda
* click for cli dev
* versioneer (cookiecutter runs install during post-installation hook)
* [pre-commit](https://pre-commit.com/) hook with black and flake8
* pytest with coverage
* Common github actions
* [pydantic](https://pydantic-docs.helpmanual.io/) for use with data structures


### Notes
Jinja templating and github actions


Conda vs pip installation
- runtime requirement should make an effor to only reference conda-forge distributions
