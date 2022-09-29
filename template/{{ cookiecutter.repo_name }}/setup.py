from setuptools import setup, find_packages
from os import path
import versioneer

cur_dir = path.abspath(path.dirname(__file__))

# parse requirements
with open(path.join(cur_dir, "requirements.txt"), "r") as f:
    requirements = f.read().split()

setup(
    name="{{ cookiecutter.package }}",
    author="{{ cookiecutter.author }}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    #  license="...",
    install_requires=requirements,
    url="{{ cookiecutter.github_url }}",
    include_package_data=True,
    python_requires=">=3.8",
    entry_points={
        "orchestration": [
            "{{ cookiecutter.package }}.model=\
                {{ cookiecutter.package }}.model:{{ cookiecutter.model_class }}",
            "{{ cookiecutter.package }}.flow=\
                {{ cookiecutter.package }}.flow:flow",
        ]
    },
)
