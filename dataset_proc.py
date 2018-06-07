#!/usr/bin/env python3
import os
import json
mydir = "./data"

data = {}
i = 0

for dirpath, dirnames, filenames in os.walk(mydir):
    if not dirnames:
        print (dirpath, "has 0 subdirectories and", len(filenames), "files")
        savedPath = os.getcwd()
        print (filenames)
        i= i+1
        my_orig = {
            'filenames' : filenames
        }
        data['orig'+str(i)] = my_orig

json_data = json.dumps(data)
print(json_data)

