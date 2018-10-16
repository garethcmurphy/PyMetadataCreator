#!/usr/bin/env bash
if [ "$(hostname)" == "login.esss.dk" ]; then
	git stash
	git pull
fi
pipenv install
pipenv run metadatacreator/GenerateMetadata.py
echo "Copying to ssh0"
scp test_new_metadata.json ssh0:

#cp datasets.json ~/CatanieDataLoad/src/
