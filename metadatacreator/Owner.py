#!/usr/bin/env python3
"""owner"""
import json
import sys


class Owner:
    """data owner"""
    def __init__(self):
        self.owner_name = "string"
        self.email = "string@string.com"
        self.owner_list = {}

    def setup(self, name, email, orcid, instrument):
        """setup owner"""
        self.owner_name = "string"
        owner = {
            "name": name,
            "email": email,
            "orcid": orcid,
        }
        self.owner_list[instrument] = owner

    def loop(self):
        """loop over owners"""
        self.setup("Francesco Piscitelli", "Francesco.Piscitelli@esss.se", "0000-0002-0325-4407", "multiblade")
        self.setup("Anton Khaplanov", "anton.khaplanov@esss.se", "0000-0002-8421-1184", "multigrid")
        self.setup("Dorothea Pfeiffer", "Dorothea.Pfeiffer@esss.se", "0000-0003-3893-2308", "nmx")
        self.setup("Ramsey Al Jebali", "ramsey.aljebali@esss.se", "0000-0000-0000-0000", "sonde")
        json.dump(self.owner_list, sys.stdout, indent=2)

        with open('owner.json', 'w') as file:
            json.dump(self.owner_list, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    OWNER = Owner()
    OWNER.loop()
