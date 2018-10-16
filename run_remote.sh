#!/usr/bin/env bash
git status
git add .
git commit -m "update metadata"
git push
ssh login "cd ~/test/PyMetadataCreator && ls"
ssh kubetest01 "cd ~/test/PyMetadataCreator && ls"
