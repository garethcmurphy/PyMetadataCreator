#!/usr/bin/env python3
import sys
import os
import json


from dataset import Dataset
from orig import Orig

class PyDatasetProcessor:
    def __init__(self):
        self.mydir = "./data"
        self.mydir = "static"
        #self.mydir = "/users/detector/experiments/multiblade/data/brightness"

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

                d= Dataset()
                my_dataset = d.dataset
                my_dataset["pid"] = "MB" + str(i).zfill(5)
                print(my_dataset["pid"])
                filelist = []
                totalfilesize = 0
                for file in filenames:
                    longname = dirpath + '/' + file
                    
                    statinfo = os.stat(longname)
                    relpath = longname.replace('/users/detector', '/static')
                    file_size = statinfo.st_size
                    totalfilesize += file_size
                    file_entry = {
                        "path": relpath,
                        "size": file_size,
                        "time": "2018-04-23T09:23:47.000Z",
                        "chk": "string",
                        "uid": "string",
                        "gid": "string",
                        "perm": "string"
                    }
                    filelist.append(file_entry)
                my_dataset["size"] = totalfilesize
                my_dataset["packedSize"] = totalfilesize
                orig = Orig()
                my_orig = orig.orig
                my_orig["size"]= totalfilesize
                my_orig["packedSize"]= totalfilesize
                my_orig["datasetId"]=  "10.17199/"+str(my_dataset["pid"])

                scicat_entries = {"dataset": my_dataset, "orig": my_orig}
                datasets["orig" + str(i).zfill(5)] = scicat_entries

        json.dump(datasets, sys.stdout, indent=2)

        with open('datasets.json', 'w') as f:
            json.dump(datasets, f, ensure_ascii=False, indent=2)



if __name__ == '__main__':
    g = PyDatasetProcessor()
    g.walk_tree()
