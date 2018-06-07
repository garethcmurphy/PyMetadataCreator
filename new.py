#!/usr/bin/env python3
import os
import json
mydir = "./"

data = {}

for dirpath, dirnames, filenames in os.walk(mydir):
    if not dirnames:
        print (dirpath, "has 0 subdirectories and", len(filenames), "files")
        savedPath = os.getcwd()
        print (filenames)



data['orig'] = filenames
json_data = json.dumps(data)
print(json_data)

