from {{ cookiecutter.package }} import __version__


{%- if cookiecutter.container_registry == "DockerHub" -%}

# Stanford Container Registry image
IMAGE = f"scr.svc.stanford.edu/{{ cookiecutter.registry_username }}/{{ cookiecutter.project_slug }}:{__version__}"

{%- elif cookiecutter.container_registry == "Stanford Container Registry" -%}

# DOCKERHUB IMAGE
IMAGE = f"registry.hub.docker.com/{{ cookiecutter.registry_username }}/{{ cookiecutter.project_slug }}:{__version__}"

{% endif %}