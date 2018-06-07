#!/usr/bin/env python3
import os
import json


class PyDatasetProcessor:
    def __init__(self):
        self.mydir ="./data"
        pass

    def walk_tree(self):

        datasets = {}
        orig_data = {}
        i = 0

        for dirpath, dirnames, filenames in os.walk(self.mydir):
            if not dirnames:
                print (dirpath, "has 0 subdirectories and", len(filenames), "files")
                savedPath = os.getcwd()
                print (filenames)
                i= i+1
                my_dataset = {
                  "principalInvestigator": "string",
                  "endTime": "2018-06-07T09:46:27.560Z",
                  "creationLocation": "string",
                  "dataFormat": "lst",
                  "scientificMetadata": {},
                  "owner": "Francesco Piscitelli",
                  "ownerEmail": "francesco.piscitelli@esss.se",
                  "orcidOfOwner": "0000-0002-0325-4407",
                  "contactEmail": "francesco.piscitelli@esss.se",
                  "sourceFolder": "string",
                  "size": 102400,
                  "packedSize": 1024000,
                  "creationTime": "2018-06-07T08:46:19.611Z",
                  "type": "string",
                  "validationStatus": "string",
                  "keywords": [
                    "string"
                  ],
                  "description": "string",
                  "userTargetLocation": "string",
                  "classification": "string",
                  "license": "ESS",
                  "version": "string",
                  "doi": "string",
                  "isPublished": True,
                  "ownerGroup": "string",
                  "accessGroups": [
                    "string"
                  ],
                  "createdBy": "string",
                  "updatedBy": "string",
                  "createdAt": "2018-06-07T08:46:19.611Z",
                  "updatedAt": "2018-06-07T08:46:19.611Z"
                }
                my_orig = {
                    "datafileList" : filenames,
                    "createdBy": "string",
                    "updatedBy": "ingestor",
                    "datasetId": "<PID>/a4ec147c-0d5d-4cfd-9fa5-893423a68729",
                    "rawDatasetId": "string",
                    "derivedDatasetId": "string",
                    "createdAt": "2018-04-23T09:23:47.918Z",
                    "updatedAt": "2018-04-23T09:59:04.506Z"
                }
                orig_data ["orig"+str(i)] = ( my_orig)
                datasets ["orig"+str(i)] = ( my_dataset)

        json_orig_data = json.dumps(orig_data)
        print(json_orig_data)
        json_datasets = json.dumps(datasets)
        print(json_datasets)

        with open('datasets.json', 'w') as f:
          json.dump(datasets, f, ensure_ascii=False)

        with open('orig.json', 'w') as f:
          json.dump(orig_data, f, ensure_ascii=False)


if __name__ == '__main__':
    g = PyDatasetProcessor( )
    g.walk_tree()
