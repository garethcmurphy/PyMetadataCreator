#!/usr/bin/env python3
import collections
import itertools
import json
import os

root = './'
files = itertools.chain.from_iterable((
    files for _, _, files in os.walk(root)
))
counter = collections.Counter(
    (os.path.basename(file_)[0:10] for file_ in files)
)
print(json.dumps(counter, indent=2))
