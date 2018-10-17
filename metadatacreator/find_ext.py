#!/usr/bin/env python3
import collections
import itertools
import json
import os
from collections import OrderedDict

root = './'
files = itertools.chain.from_iterable((
    files for _, _, files in os.walk(root)
))
counter = collections.Counter(
    (os.path.splitext(file_)[1] for file_ in files)
)
# counter_sorted= sorted(counter, key=counter.get)
# for w in sorted(counter, key=counter.get, reverse=True):
#  print w, counter[w]


sc = OrderedDict(sorted(counter.items(), key=lambda t: t[1], reverse=True))

print(json.dumps(sc, indent=2))
