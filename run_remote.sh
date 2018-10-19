#!/usr/bin/env bash
pipenv run ./metadatacreator/SondeImport.py
git status
git add .
git commit -m "update metadata"
git push
ssh login "cd ~/test/PyMetadataCreator && ./generate_metadata.sh"
ssh kubetest01 "cd ~/CatanieDataLoad && ./cmd2.sh"
