#!/usr/bin/env bash

versioneer install

# create git repository
git init
git add .
git commit -a -m "Initial Cookiecutter Commit."