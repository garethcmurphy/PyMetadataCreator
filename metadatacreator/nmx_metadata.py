#!/usr/bin/env python3
import json


class NmxMetadata:

    def __init__(self):
        with open('nmx.json') as json_data:
            self.metadata_object = json.load(json_data)


if __name__ == '__main__':
    nmx = NmxMetadata()
    print(nmx.metadata_object)
