#!/usr/bin/env bash
git stash
git pull
pipenv install
pipenv run metadatacreator/GenerateMetadata.py
echo "Copying to ssh0"
scp test_new_metadata.json ssh0:

#cp datasets.json ~/CatanieDataLoad/src/
