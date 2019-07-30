#!/usr/bin/env python3
"""nmx metadata"""
import json


class NmxMetadata:
    """nmx metadata"""

    def __init__(self):
        with open('nmx.json') as json_data:
            self.metadata_object = json.load(json_data)


if __name__ == '__main__':
    NMX = NmxMetadata()
    print(NMX.metadata_object)
