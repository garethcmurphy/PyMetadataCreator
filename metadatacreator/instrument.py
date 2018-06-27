#!/usr/bin/env python3
class Instrument:

    def __init__(self):
        self.owner = "ESS"
        self.ownerEmail = "undefined@esss.se"
        self.orcidOfOwner = "0000-0000-0000-0000"
        self.contactEmail = "undefined@esss.se"
        self.principal_investigator = "ESS"

    def factory( instrument_type=None):
        if instrument_type == "sonde":
            return Sonde()
        if instrument_type == "multiblade":
            return Multiblade()
        if instrument_type == "multigrid":
            return Multigrid()
        if instrument_type == "nmx":
            return Nmx()
    factory = staticmethod(factory)


class Sonde(Instrument):

    def __init__(self):
        self.owner = "Ramsey Al Jebali"
        self.ownerEmail = "ramsey.aljebali@esss.se"
        self.orcidOfOwner = "0000-0000-0000-0000"
        self.contactEmail = "ramsey.aljebali@esss.se"
        self.principal_investigator = "Ramsey Al Jebali"


class Multiblade(Instrument):

    def __init__(self):
        self.owner = "Francesco Piscitelli"
        self.ownerEmail = "Francesco.Piscitelli@esss.se"
        self.orcidOfOwner = "0000-0002-0325-4407"
        self.contactEmail = "Francesco.Piscitelli@esss.se"
        self.principal_investigator = "Francesco Piscitelli"


class Multigrid(Instrument):
    def __init__(self):
        self.owner = "Anton Khaplanov"
        self.ownerEmail = "anton.khaplanov@esss.se"
        self.orcidOfOwner = "0000-0002-8421-1184"
        self.contactEmail = "anton.khaplanov@esss.se"
        self.principal_investigator = "Anton Khaplanov"


class Nmx(Instrument):
    def __init__(self):
        self.owner = "Dorothea Pfeiffer"
        self.ownerEmail = "Dorothea.Pfeiffer@esss.se"
        self.orcidOfOwner = "0000-0003-3893-2308"
        self.contactEmail = "Dorothea.Pfeiffer@esss.se"
        self.principal_investigator = "Dorothea Pfeiffer"


if __name__ == '__main__':
    sonde = Instrument.factory("sonde")
    print(sonde.ownerEmail)
