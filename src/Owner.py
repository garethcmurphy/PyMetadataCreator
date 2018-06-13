#!/usr/bin/env python3
import sys
import json


class Owner:
    def __init__(self):
        self.owner_name = "string"
        self.email = "string@string.com"
        self.owner_list = {}

    def setup(self, name, email, orcid, instrument):
        self.owner_name = "string"
        owner = {
            "name": name,
            "email": email,
            "orcid": orcid,
        }
        self.owner_list[instrument] = owner

    def loop(self):
        self.setup("Joe Smith", "joe.smith@esss.se", "0002", "MultiBlade")
        json.dump(self.owner_list, sys.stdout, indent=2)

        with open('owner.json', 'w') as f:
            json.dump(self.owner_list, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    o = Owner()
    o.loop()
