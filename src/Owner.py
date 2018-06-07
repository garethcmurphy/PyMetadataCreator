#!/usr/bin/env python3
class Owner:
    def __init__(self):
        self.x = 2
        self.owner_name = "string"
        self.email = "string@string.com"
        self.owner_list = {}

    def setup(self, name, email, instrument):
        self.owner_name = "string"
        owner = {
            "name": name,
            "email": email
        }
        self.owner_list[instrument] = owner

    def loop(self):
        self.setup("Joe Bloggs", "joe.bloggs@esss.se", "MultiBlade")
