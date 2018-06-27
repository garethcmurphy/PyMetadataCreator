#!/usr/bin/env python3
class Instrument:

    def __init__(self):
        self.inst = {'owner': "ESS",
                     'ownerEmail': "undefined@esss.se",
                     'orcidOfOwner': "0000-0000-0000-0000",
                     'contactEmail': "undefined@esss.se",
                     'principal_investigator': "ESS"
                     }

    def factory(instrument_type=None):
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
        self.inst = {'owner': "Ramsey Al Jebali",
                     'ownerEmail': "ramsey.aljebali@esss.se",
                     'orcidOfOwner': "0000-0000-0000-0000",
                     'contactEmail': "ramsey.aljebali@esss.se",
                     'principal_investigator': "Ramsey Al Jebali",
                     }


class Multiblade(Instrument):

    def __init__(self):
        self.inst = {'owner': "Francesco Piscitelli",
                     'ownerEmail': "Francesco.Piscitelli@esss.se",
                     'orcidOfOwner': "0000-0002-0325-4407",
                     'contactEmail': "Francesco.Piscitelli@esss.se",
                     'principal_investigator': "Francesco Piscitelli"
                     }


class Multigrid(Instrument):
    def __init__(self):
        self.inst = {'owner': "Anton Khaplanov",
                     'ownerEmail': "anton.khaplanov@esss.se",
                     'orcidOfOwner': "0000-0002-8421-1184",
                     'contactEmail': "anton.khaplanov@esss.se",
                     'principal_investigator': "Anton Khaplanov",
                     }


class Nmx(Instrument):
    def __init__(self):
        self.inst = {'owner': "Dorothea Pfeiffer",
                     'ownerEmail': "Dorothea.Pfeiffer@esss.se",
                     'orcidOfOwner': "0000-0003-3893-2308",
                     'contactEmail': "Dorothea.Pfeiffer@esss.se",
                     'principal_investigator': "Dorothea Pfeiffer",
                     }


if __name__ == '__main__':
    sonde = Instrument.factory("sonde")
    print(sonde.inst)
