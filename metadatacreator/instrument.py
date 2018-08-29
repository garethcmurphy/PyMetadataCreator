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
        if instrument_type == 'v20':
            return V20()
        if instrument_type == 'hzb':
            return Hzb()
        if instrument_type == 'ife':
            return Ife()
        if instrument_type == 'ess':
            return Ess()

    factory = staticmethod(factory)


class DefaultInst(Instrument):

    def __init__(self):
        self.abbreviation = 'SONDE'
        self.doi = '10.17199/BRIGHTNESS/SONDE0001'
        self.affiliation = 'ESS'
        self.creator = 'ESS'
        self.publisher = 'ESS'
        self.publicationYear = 2017
        self.title = 'Sample Data from SONDE'
        self.url = 'https://scicat.esss.se/datasets/10.17199%2FBRIGHTNESS%2FSONDE0001'
        self.abstract = """This data was collected as part of BrightnESS, funded by the European Union \
                        Framework Programme for Research and Innovation Horizon 2020, under grant \
                        agreement 676548. It consists of test data for the detector."""
        self.resourceType = 'NeXus HDF5 files'
        self.sizeOfArchive = 33.1
        self.numberOfFiles = 11
        self.pidArray = ['string']
        self.authors = ['string']
        self.doiRegisteredSuccessfullyTime = "2018"

        self.source_folder_array = ['subfolder']

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
        self.abbreviation = 'SONDE'
        self.doi = '10.17199/BRIGHTNESS/SONDE0001'
        self.affiliation = 'ESS'
        self.creator = 'Ramsey Al Jebali'
        self.publisher = 'ESS'
        self.publicationYear = 2017
        self.title = 'Sample Data from SONDE'
        self.url = 'https://scicat.esss.se/datasets/10.17199%2FBRIGHTNESS%2FSONDE0001'
        self.abstract = """This data was collected as part of BrightnESS, funded by the European Union \
                        Framework Programme for Research and Innovation Horizon 2020, under grant \
                        agreement 676548. It consists of test data for the detector."""
        self.resourceType = 'NeXus HDF5 files'
        self.sizeOfArchive = 33.1
        self.numberOfFiles = 11
        self.pidArray = ['string']
        self.authors = ['string']
        self.doiRegisteredSuccessfullyTime = "2018"

        self.source_folder_array = [
            'sonde/IFE_june_2018/data/S1',
            'sonde/IFE_june_2018/data/S2'
        ]

        self.inst = {'owner': '',
                     'ownerEmail': 'ramsey.aljebali@esss.se',
                     'orcidOfOwner': '0000-0000-0000-0000',
                     'contactEmail': 'ramsey.aljebali@esss.se',
                     'principalInvestigator': 'Ramsey Al Jebali',
                     'userTargetLocation': 'SONDE',
                     'sourceFolder': 'sonde/IFE_june_2018/data/S1',
                     'creationLocation': 'SONDE',
                     }


class Multiblade(Instrument):

    def __init__(self):
        self.abbreviation = 'MB'
        self.doi = '10.17199/BRIGHTNESS/MB0001'
        self.affiliation = 'ESS'
        self.creator = 'Francesco Piscitelli'
        self.publisher = 'ESS'
        self.publicationYear = 2017
        self.title = 'Sample Data from Multiblade'
        self.url = 'https://scicat.esss.se/datasets/10.17199%2FBRIGHTNESS%2FMB0001'
        self.abstract = """This data was collected as part of BrightnESS, funded by the European Union \
                        Framework Programme for Research and Innovation Horizon 2020, under grant \
                        agreement 676548. It consists of test data for the detector."""
        self.resourceType = 'NeXus HDF5 files'
        self.sizeOfArchive = 33.1
        self.numberOfFiles = 11
        self.pidArray = ['string']
        self.authors = ['string']
        self.doiRegisteredSuccessfullyTime = "2018"

        self.source_folder_array = [
            'multiblade/data/brightness/2017_06_BNC_MB16T_ElectronicsTests/DATA',
            'multiblade/data/brightness/2016_03_BNC_MB15_DetectorCharacterization_1/ReducedData/160304_000_output_duringBeamTime_obsolete/20160303_output_tests/'
        ]
        self.inst = {'owner': 'Francesco Piscitelli',
                     'ownerEmail': 'Francesco.Piscitelli@esss.se',
                     'orcidOfOwner': '0000-0002-0325-4407',
                     'contactEmail': 'Francesco.Piscitelli@esss.se',
                     'principalInvestigator': 'Francesco Piscitelli',
                     'userTargetLocation': 'multiblade',
                     'sourceFolder': 'multiblade/data/brightness/2017_06_BNC_MB16T_ElectronicsTests/DATA',
                     'creationLocation': 'multiblade',
                     }


class Multigrid(Instrument):
    def __init__(self):
        self.abbreviation = 'MG'
        self.doi = '10.17199/BRIGHTNESS/MG0001'
        self.affiliation = 'ESS'
        self.creator = 'Anton Khaplanov'
        self.publisher = 'ESS'
        self.publicationYear = 2017
        self.title = 'Sample Data from Multigrid'
        self.url = 'https://scicat.esss.se/datasets/10.17199%2FBRIGHTNESS%2FMG0001'
        self.abstract = """This data was collected as part of BrightnESS, funded by the European Union \
                        Framework Programme for Research and Innovation Horizon 2020, under grant \
                        agreement 676548. It consists of test data for the detector."""
        self.resourceType = 'NeXus HDF5 files'
        self.sizeOfArchive = 33.1
        self.numberOfFiles = 11
        self.pidArray = ['string']
        self.authors = ['string']
        self.doiRegisteredSuccessfullyTime = "2018"

        self.source_folder_array = [
            'multigrid/data/raw/MG_CNCS/07_13_7p2A',
            'multigrid/data/raw/MG_CNCS/07_14'
        ]

        self.inst = {'owner': 'Anton Khaplanov',
                     'ownerEmail': 'anton.khaplanov@esss.se',
                     'orcidOfOwner': '0000-0002-8421-1184',
                     'contactEmail': 'anton.khaplanov@esss.se',
                     'principalInvestigator': 'Anton Khaplanov',
                     'userTargetLocation': 'multigrid',
                     'sourceFolder': 'multigrid/data/raw/MG_CNCS/07_14',
                     'creationLocation': 'multigrid',
                     }


class Nmx(Instrument):
    def __init__(self):
        self.abbreviation = 'NMX'
        self.doi = '10.17199/BRIGHTNESS/NMX0001'
        self.affiliation = 'ESS'
        self.creator = 'Dorothea Pfeiffer'
        self.publisher = 'ESS'
        self.publicationYear = 2017
        self.title = 'Sample Data from NMX'
        self.url = 'https://scicat.esss.se/datasets/10.17199%2FBRIGHTNESS%2FNMX0001'
        self.abstract = """This data was collected as part of BrightnESS, funded by the European Union \ 
                        Framework Programme for Research and Innovation Horizon 2020, under grant \
                        agreement 676548. It consists of test data for the detector."""
        self.resourceType = 'NeXus HDF5 files'
        self.sizeOfArchive = 33.1
        self.numberOfFiles = 11
        self.pidArray = ['string']
        self.authors = ['string']
        self.doiRegisteredSuccessfullyTime = "2018"

        self.source_folder_array = [
            'nmx/data/h5/raw/IFE_2016_Nov/APZ_threshold_scan/',
            'nmx/data/h5/raw/IFE_2016_Nov/Calibration/'
        ]

        self.inst = {'owner': 'Dorothea Pfeiffer',
                     'ownerEmail': 'Dorothea.Pfeiffer@esss.se',
                     'orcidOfOwner': '0000-0003-3893-2308',
                     'contactEmail': 'Dorothea.Pfeiffer@esss.se',
                     'principalInvestigator': 'Dorothea Pfeiffer',
                     'userTargetLocation': 'NMX',
                     'sourceFolder': 'nmx/data/h5/raw/IFE_2016_Nov',
                     'creationLocation': 'NMX',
                     }


class V20(Instrument):
    def __init__(self):
        self.abbreviation = 'V20'
        self.affiliation = 'ESS'
        self.publisher = 'ESS'
        self.inst = {'owner': 'Jonas Nilsson',
                     'ownerEmail': 'jonas.nilsson@esss.se',
                     'orcidOfOwner': '0000-0003-3893-2308',
                     'contactEmail': 'jonas.nilsson@esss.se',
                     'principalInvestigator': 'Jonas Nilsson',
                     'userTargetLocation': 'V20',
                     'sourceFolder': 'V20',
                     'creationLocation': 'V20',
                     }


class Hzb(Instrument):
    def __init__(self):
        self.abbreviation = 'HZB'
        self.affiliation = 'ESS'
        self.publisher = 'ESS'
        self.inst = {'owner': 'Jonas Nilsson',
                     'ownerEmail': 'jonas.nilsson@esss.se',
                     'orcidOfOwner': '0000-0003-3893-2308',
                     'contactEmail': 'jonas.nilsson@esss.se',
                     'principalInvestigator': 'Jonas Nilsson',
                     'userTargetLocation': 'HZB',
                     'sourceFolder': 'HZB',
                     'creationLocation': 'HZB',
                     }


class Ife(Instrument):
    def __init__(self):
        self.abbreviation = 'IFE'
        self.inst = {'owner': 'Jonas Nilsson',
                     'ownerEmail': 'jonas.nilsson@esss.se',
                     'orcidOfOwner': '0000-0003-3893-2308',
                     'contactEmail': 'jonas.nilsson@esss.se',
                     'principalInvestigator': 'Jonas Nilsson',
                     'userTargetLocation': 'IFE',
                     'sourceFolder': 'IFE',
                     'creationLocation': 'IFE',
                     }


class Ess(Instrument):
    def __init__(self):
        self.abbreviation = 'ESS'
        self.affiliation = 'ESS'
        self.publisher = 'ESS'
        self.inst = {'owner': 'Jonas Nilsson',
                     'ownerEmail': 'jonas.nilsson@esss.se',
                     'orcidOfOwner': '0000-0003-3893-2308',
                     'contactEmail': 'jonas.nilsson@esss.se',
                     'principalInvestigator': 'Jonas Nilsson',
                     'userTargetLocation': 'ESS',
                     'sourceFolder': 'ESS',
                     'creationLocation': 'ESS',
                     }


if __name__ == '__main__':
    sonde = Instrument.factory('sonde')
    print(sonde.inst)
