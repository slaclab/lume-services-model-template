from pkg_resources import resource_filename

VARIABLE_FILE = resource_filename("{{ cookiecutter.project_slug }}.files", "variables.yml")