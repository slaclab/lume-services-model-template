from {{ cookiecutter.package }} import __version__

{%- if cookiecutter.container_registry == "DockerHub" -%}

# DOCKERHUB IMAGE
IMAGE = f"registry.hub.docker.com/{{ cookiecutter.registry_username }}/{{ cookiecutter.repo_name }}:v{__version__}"

{%- elif cookiecutter.container_registry == "Stanford Container Registry" -%}

# Stanford Container Registry image
IMAGE = f"scr.svc.stanford.edu/{{ cookiecutter.registry_username }}/{{ cookiecutter.repo_name }}:v{__version__}"

{% endif %}
