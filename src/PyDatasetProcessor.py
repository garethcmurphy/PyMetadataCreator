#!/usr/bin/env python3
import json
import os
import sys

from dataset import Dataset
from orig import Orig


class PyDatasetProcessor:
    def __init__(self):
        self.mydir = "./data"
        self.mydir = "static"
        # self.mydir = "/users/detector/experiments/multiblade/data/brightness"

    def walk_tree(self):

        datasets = {}
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

                d = Dataset()
                my_data_set = d.dataset
                my_data_set["pid"] = "MB" + str(i).zfill(5)
                print(my_data_set["pid"])
                file_list = []
                total_file_size = 0
                for file in filenames:
                    longname = dirpath + '/' + file

                    statinfo = os.stat(longname)
                    relpath = longname.replace('/users/detector', '/static')
                    file_size = statinfo.st_size
                    total_file_size += file_size
                    file_entry = {
                        "path": relpath,
                        "size": file_size,
                        "time": "2018-04-23T09:23:47.000Z",
                        "chk": "string",
                        "uid": "string",
                        "gid": "string",
                        "perm": "string"
                    }
                    file_list.append(file_entry)
                my_data_set["size"] = total_file_size
                my_data_set["packedSize"] = total_file_size
                orig = Orig()
                my_orig = orig.orig
                my_orig["size"] = total_file_size
                my_orig["packedSize"] = total_file_size
                my_orig["datasetId"] = "10.17199/" + str(my_data_set["pid"])

                scicat_entries = {"dataset": my_data_set, "orig": my_orig}
                datasets["orig" + str(i).zfill(5)] = scicat_entries

        json.dump(datasets, sys.stdout, indent=2)

        with open('datasets.json', 'w') as f:
            json.dump(datasets, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    g = PyDatasetProcessor()
    g.walk_tree()
