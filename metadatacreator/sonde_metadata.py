#!/usr/bin/env python3
import json


class SondeMetadata:

    def __init__(self):
        with open('sonde.json') as json_data:
            self.metadata_object = json.load(json_data)


if __name__ == '__main__':
    nmx = SondeMetadata()
    print(nmx.metadata_object)
