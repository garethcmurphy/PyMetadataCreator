#!/usr/bin/env python3
class Instrument:

    def factory(instrument_type=None):
        if instrument_type == 'sonde':
            return Sonde()
        if instrument_type == 'multiblade':
            return Multiblade()
        if instrument_type == 'multigrid':
            return Multigrid()
        if instrument_type == 'nmx':
            return Nmx()

    factory = staticmethod(factory)


class DefaultInst(Instrument):

    def __init__(self):
        self.inst = {'owner': 'ESS',
                     'ownerEmail': 'undefined@esss.se',
                     'orcidOfOwner': '0000-0000-0000-0000',
                     'contactEmail': 'undefined@esss.se',
                     'principalInvestigator': 'ESS',
                     'userTargetLocation': 'ESS',
                     'sourceFolder': 'ESS',
                     'creationLocation': 'ESS',
                     }


class Sonde(Instrument):

    def __init__(self):
        self.abbreviation = 'SON'
        self.inst = {'owner': 'Ramsey Al Jebali',
                     'ownerEmail': 'ramsey.aljebali@esss.se',
                     'orcidOfOwner': '0000-0000-0000-0000',
                     'contactEmail': 'ramsey.aljebali@esss.se',
                     'principalInvestigator': 'Ramsey Al Jebali',
                     'userTargetLocation': 'ESS',
                     'sourceFolder': 'ESS',
                     'creationLocation': 'ESS',
                     }


class Multiblade(Instrument):

    def __init__(self):
        self.abbreviation = 'MB'
        self.inst = {'owner': 'Francesco Piscitelli',
                     'ownerEmail': 'Francesco.Piscitelli@esss.se',
                     'orcidOfOwner': '0000-0002-0325-4407',
                     'contactEmail': 'Francesco.Piscitelli@esss.se',
                     'principalInvestigator': 'Francesco Piscitelli',
                     'userTargetLocation': 'multiblade',
                     'sourceFolder': 'multiblade',
                     'creationLocation': 'multiblade',
                     }


class Multigrid(Instrument):
    def __init__(self):
        self.abbreviation = 'MG'
        self.inst = {'owner': 'Anton Khaplanov',
                     'ownerEmail': 'anton.khaplanov@esss.se',
                     'orcidOfOwner': '0000-0002-8421-1184',
                     'contactEmail': 'anton.khaplanov@esss.se',
                     'principalInvestigator': 'Anton Khaplanov',
                     'userTargetLocation': 'multigrid',
                     'sourceFolder': 'multigrid',
                     'creationLocation': 'multigrid',
                     }


class Nmx(Instrument):
    def __init__(self):
        self.abbreviation = 'NMX'
        self.inst = {'owner': 'Dorothea Pfeiffer',
                     'ownerEmail': 'Dorothea.Pfeiffer@esss.se',
                     'orcidOfOwner': '0000-0003-3893-2308',
                     'contactEmail': 'Dorothea.Pfeiffer@esss.se',
                     'principalInvestigator': 'Dorothea Pfeiffer',
                     'userTargetLocation': 'NMX',
                     'sourceFolder': 'NMX',
                     'creationLocation': 'NMX',
                     }


if __name__ == '__main__':
    sonde = Instrument.factory('sonde')
    print(sonde.inst)
