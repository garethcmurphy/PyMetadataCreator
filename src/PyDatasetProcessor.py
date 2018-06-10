#!/usr/bin/env python
import json
import os


class PyDatasetProcessor:
    def __init__(self):
        self.mydir = "./data"
        self.mydir = "static"
        self.mydir = "/users/detector/experiments/multiblade/data/brightness"
        pass

    def walk_tree(self):

        datasets = {}
        orig_data = {}
        i = 0

        for dirpath, dirnames, filenames in os.walk(self.mydir):
            if not dirnames:
                print(dirpath, "has 0 subdirectories and", len(filenames), "files")
                print(filenames)
                i = i + 1
                basename = os.path.basename(dirpath)
                year = "2018"
                if basename[:3] == '201':
                    year = basename[:4]
                print('gm', year)

                my_dataset = {
                    "principalInvestigator": "string",
                    "endTime": "2018-06-07T09:46:27.560Z",
                    "creationLocation": "Multiblade",
                    "dataFormat": "lst",
                    "scientificMetadata": {},
                    "owner": "Francesco Piscitelli",
                    "ownerEmail": "francesco.piscitelli@esss.se",
                    "orcidOfOwner": "0000-0002-0325-4407",
                    "contactEmail": "francesco.piscitelli@esss.se",
                    "sourceFolder": "multiblade",
                    "proposalId": "2018ESS1",
                    "size": 102400,
                    "pid": "MB" + str(i).zfill(5),
                    "packedSize": 1024000,
                    "creationTime": "2018-06-07T08:46:19.611Z",
                    "type": "raw",
                    "validationStatus": "valid",
                    "keywords": [
                        "Vanadium"
                    ],
                    "description": "string",
                    "userTargetLocation": "Multiblade",
                    "classification": "analyzed",
                    "license": "ESS",
                    "version": "v1",
                    "doi": "replace with doi",
                    "isPublished": True,
                    "ownerGroup": "brightness",
                    "accessGroups": [
                        "brightness"
                    ],
                    "createdBy": "ingestor",
                    "updatedBy": "ingestor",
                    "createdAt": "2018-06-07T08:46:19.611Z",
                    "updatedAt": "2018-06-07T08:46:19.611Z"
                }
                filelist = []
                for file in filenames:
                    longname = dirpath + '/' + file
                    
                    statinfo = os.stat(longname)
                    relpath = longname.replace('/users/detector', '/static')
                    file_entry = {
                        "path": relpath,
                        "size": statinfo.st_size,
                        "time": "2018-04-23T09:23:47.000Z",
                        "chk": "string",
                        "uid": "string",
                        "gid": "string",
                        "perm": "string"
                    }
                    filelist.append(file_entry)
                my_orig = {
                    "size": 0,
                    "dataFileList": filelist,
                    "ownerGroup": "brightness",
                    "accessGroups": [
                        "brightness"
                    ],
                    "createdBy": "ingestor",
                    "updatedBy": "ingestor",
                    "datasetId": "10.17199/"+my_dataset["pid"],
                    "rawDatasetId": "string",
                    "derivedDatasetId": "string",
                    "createdAt": "2018-04-23T09:23:47.918Z",
                    "updatedAt": "2018-04-23T09:59:04.506Z"
                }
                scicat_entries = {"dataset": my_dataset, "orig": my_orig}
                orig_data["orig" + str(i)] = my_orig
                datasets["orig" + str(i)] = scicat_entries

        json_orig_data = json.dumps(orig_data)
        print(json_orig_data)
        json_datasets = json.dumps(datasets)
        print(json_datasets)

        with open('datasets.json', 'w') as f:
            json.dump(datasets, f, ensure_ascii=False)

        with open('orig.json', 'w') as f:
            json.dump(orig_data, f, ensure_ascii=False)


if __name__ == '__main__':
    g = PyDatasetProcessor()
    g.walk_tree()
