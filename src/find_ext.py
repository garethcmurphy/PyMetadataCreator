#!/usr/bin/env python2
import json
import collections
import itertools
import os

root = './'
files = itertools.chain.from_iterable((
    files for _,_,files in os.walk(root)
    ))
counter = collections.Counter(
    (os.path.splitext(file_)[1] for file_ in files)
)
print (json.dumps(counter, indent=2))
