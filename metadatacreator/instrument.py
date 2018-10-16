#!/usr/bin/env python3
import datetime

import pytz

from multiblade_metadata import MultibladeMetadata
from nmx_metadata import NmxMetadata
from sonde_metadata import SondeMetadata
from multigrid_metadata import MultigridMetadata


class Instrument:
    doi_prefix = "10.17199/BRIGHTNESS/"
    handle_prefix = "20.500.12269"
    url_fragment = 'https://scicat.esss.se/datasets/' + handle_prefix + "%2FBRIGHTNESS%2F"

    def __init__(self):
        pass

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


class DefaultInst:
    doi_prefix = "10.17199/BRIGHTNESS/"
    handle_prefix = "20.500.12269"
    url_fragment = 'https://scicat.esss.se/datasets/' + handle_prefix + "%2FBRIGHTNESS%2F"
    abbreviation = 'SONDE'

    url = url_fragment + abbreviation
    dataDescription = 'https://github.com/ess-dmsc/ess_file_formats/wiki/SONDE'
    affiliation = 'ESS'
    creator = 'Ramsey Al Jebali'
    publisher = 'ESS'
    publicationYear = 2018

    principalInvestigator = creator
    endTime = datetime.datetime.now(tz=pytz.utc).isoformat()
    creationLocation = abbreviation
    owner = creator
    ownerEmail = 'ramsey.aljebali@esss.se'
    orcidOfOwner = '0000-0000-0000-0000'
    contactEmail = ownerEmail
    sourceFolder = 'sonde/IFE_june_2018/data/S13'
    size = 10
    packedSize = 10
    creationTime = endTime
    type = "raw"
    validationStatus = "valid"
    keywords = [abbreviation, 'IFE']
    description = dataDescription
    title = 'Sample Data from ' + abbreviation
    userTargetLocation = abbreviation
    classification = "valid"
    license = "ESS"
    version = "v1"
    doi = doi_prefix + abbreviation
    isPublished = True
    ownerGroup = 'ess'
    accessGroups = ['brightness', 'ess', 'loki']
    isPublished = True
    createdBy = "ingestor"
    updatedBy = "ingestor"
    createdAt = endTime
    updatedAt = endTime
    sampleId = "SAMPLE001"

    abstract = """This data was collected as part of BrightnESS, funded by the European Union 
      Framework Programme for Research and Innovation Horizon 2020, under grant 
      agreement 676548. It consists of test data for the detector."""
    resourceType = 'Comma Separated Variable (csv) files'
    sizeOfArchive = 33.1
    numberOfFiles = 11
    pidArray = ['string']
    authors = [owner]
    doiRegisteredSuccessfullyTime = "2018"
    proposal = '2018ESS2'

    isOnDisk = True
    isOnTape = True
    isOnCentralDisk = True
    archivable = True
    retrievable = True
    archiveStatusMessage = "datasetCreated"
    retrieveStatusMessage = "string"
    lastUpdateMessage = "string"
    archiveReturnMessage = "string"
    MessageHistory = [
        {
            "id": "string",
            "shortMessage": "string",
            "sender": "string",
            "when": "now",
            "payload": {}
        }
    ]
    dateOfLastMessage = endTime
    dateOfDiskPurging = endTime
    archiveRetentionTime = endTime
    isExported = True
    exportedTo = "string"
    dateOfPublishing = endTime

    metadata_object = {
        '0001': {"wavelength": 2},
        '0048': {"wavelength": 2}
    }


class Multigrid(DefaultInst):
    def __init__(self):
        self.abbreviation = 'MG'

        self.owner = 'Anton Khaplanov'
        self.ownerEmail = 'anton.khaplanov@esss.se'

        self.sourceFolder = 'multigrid/data/raw/MG_CNCS/07_14'
        self.orcidOfOwner = '0000-0002-8421-1184'
        self.contactEmail = self.ownerEmail
        self.principalInvestigator = self.owner
        self.userTargetLocation = 'multigrid'
        self.creationLocation = self.creationLocation
        self.keywords = [self.abbreviation]

        self.doi = self.doi_prefix + self.abbreviation
        self.creator = self.owner
        self.title = 'Sample Data from Multigrid'
        self.url = self.url_fragment + self.abbreviation
        self.dataDescription = 'https://github.com/ess-dmsc/ess_file_formats/wiki/Multigrid-Data-Format-I'
        self.abstract = """This data was collected as part of BrightnESS, funded by the European Union 
                        Framework Programme for Research and Innovation Horizon 2020, under grant 
                        agreement 676548. It consists of test data for the detector."""
        self.resourceType = 'raw binary files'
        self.pidArray = ['string']
        self.authors = [self.owner]
        self.doiRegisteredSuccessfullyTime = "2018"
        self.scientificMetadata = {
            'id': 3
        }
        self.proposal = '2018ESS3'

        self.source_folder_array = {
            '0001': 'multigrid/data/raw/MG_CNCS/07_11/beamOn_resetOn',
            '0002': 'multigrid/data/raw/MG_CNCS/07_11/no_reset',
            '0003': 'multigrid/data/raw/MG_CNCS/07_12_background',
            '0004': 'multigrid/data/raw/MG_CNCS/07_13_12A',
            '0005': 'multigrid/data/raw/MG_CNCS/07_13_12A_Vanadium_powder',
            '0006': 'multigrid/data/raw/MG_CNCS/07_13_4p96A',
            '0007': 'multigrid/data/raw/MG_CNCS/07_13_7p2A',
            '0008': 'multigrid/data/raw/MG_CNCS/07_13_7p2A/1_t0_timing',
            '0009': 'multigrid/data/raw/MG_CNCS/07_14',
            '0010': 'multigrid/data/raw/MG_CNCS/07_15',
            '0011': 'multigrid/data/raw/MG_CNCS/07_25',
            '0012': 'multigrid/data/raw/MG_CNCS/08_16',
            '0013': 'multigrid/data/raw/MG_CNCS/09_29',
            '0014': 'multigrid/data/raw/MG_CNCS/10_13',
            '0015': 'multigrid/data/raw/MG_CNCS/11_29',
        }
        fetch_metadata = MultigridMetadata()
        self.metadata_object = fetch_metadata.metadata_object

class Nmx(DefaultInst):
    def __init__(self):
        self.abbreviation = 'NMX'

        self.owner = 'Dorothea Pfeiffer'
        self.ownerEmail = 'Dorothea.Pfeiffer@esss.se'
        self.sourceFolder = 'nmx/data/h5/raw/IFE_2016_Nov'
        self.orcidOfOwner = '0000-0003-3893-2308'
        self.contactEmail = self.ownerEmail
        self.principalInvestigator = self.owner
        self.userTargetLocation = self.abbreviation
        self.creationLocation = self.abbreviation
        self.keywords = [self.abbreviation]

        self.doi = self.doi_prefix + self.abbreviation
        self.creator = self.owner
        self.title = 'Sample Data from NMX'
        self.url = self.url_fragment + self.abbreviation
        self.dataDescription = 'https://github.com/ess-dmsc/ess_file_formats/wiki/NMX'
        self.abstract = """This data was collected as part of BrightnESS, funded by the European Union  
                        Framework Programme for Research and Innovation Horizon 2020, under grant 
                        agreement 676548. It consists of test data for the detector."""
        self.resourceType = 'NeXus HDF5 files'
        self.pidArray = ['string']
        self.authors = [self.owner]
        self.scientificMetadata = {
            'instrument': 'Sisi',
            'purpose': 'calibration',
            'F+GEM V': '33330',
            'D field kV/cm': '1',
            'F+D V': '3948',
            'Config': 'back',
            'Wavelength': '2',
            'Beam': 'unfocused',
            'Collimator (Material (w x h) AlBO3': '10x20',
            'Collimator (Material (w x h) B4C': '20x30',
            'Collimator (Material (w x h) AlBO3 2': '10x10',
            'Collimator (Material (w x h) B4C 2': '10x30',
            'Collimator (Material (w x h) B4C 3': '30x10',
            'Collimator (Material (w x h) B4C sum': '10x10',
            'Mask': 'none',
            'MCA': '60',
            'He3': '10',
            'Run number': '132',
            '1E3 hits': '500',
            'Chip': 'APV25',
            'ZS': 'APZ',
            'Threshold': '280',
        }
        self.proposal = '2018ESS4'

        self.source_folder_array = {
            '0001': 'nmx/data/h5/analyzed/dead200dead600/IFE_2015_Feb',
            '0002': 'nmx/data/h5/analyzed/parameters',
            '0003': 'nmx/data/h5/analyzed/thresh100_150',
            '0004': 'nmx/data/h5/analyzed/thresh100_150/IFE_2015_Feb',
            '0005': 'nmx/data/h5/analyzed/thresh100_150/IFE_2016_Jun',
            '0006': 'nmx/data/h5/analyzed/thresh100_150/IFE_2016_Nov',
            '0007': 'nmx/data/h5/analyzed/thresh100_150/IFE_2016_Nov/APZ_threshold_scan',
            '0010': 'nmx/data/h5/analyzed/thresh100_150/IFE_2016_Nov/Calibration',
            '0011': 'nmx/data/h5/analyzed/thresh100_150/IFE_2016_Nov/Efficiency',
            '0012': 'nmx/data/h5/analyzed/thresh100_150/IFE_2016_Nov/Pattern',
            '0013': 'nmx/data/h5/analyzed/thresh100_150/IFE_2016_Nov/Scattering',
            '0014': 'nmx/data/h5/apv2vmm/IFE_2015_Feb',
            '0015': 'nmx/data/h5/apv2vmm/IFE_2016_Jun',
            '0016': 'nmx/data/h5/apv2vmm/IFE_2016_Nov',
            '0017': 'nmx/data/h5/apv2vmm/IFE_2016_Nov/APZ_threshold_scan',
            '0020': 'nmx/data/h5/apv2vmm/IFE_2016_Nov/Calibration',
            '0021': 'nmx/data/h5/apv2vmm/IFE_2016_Nov/Efficiency',
            '0022': 'nmx/data/h5/apv2vmm/IFE_2016_Nov/Pattern',
            '0023': 'nmx/data/h5/apv2vmm/IFE_2016_Nov/Scattering',
            '0024': 'nmx/data/h5/raw/IFE_2015_Feb',
            '0025': 'nmx/data/h5/raw/IFE_2016_Jun',
            '0026': 'nmx/data/h5/raw/IFE_2016_Nov',
            '0027': 'nmx/data/h5/raw/IFE_2016_Nov/APZ_threshold_scan',
            '0030': 'nmx/data/h5/raw/IFE_2016_Nov/Calibration',
            '0031': 'nmx/data/h5/raw/IFE_2016_Nov/Efficiency',
            '0032': 'nmx/data/h5/raw/IFE_2016_Nov/Pattern',
            '0033': 'nmx/data/h5/raw/IFE_2016_Nov/Scattering',
            '0034': 'nmx/data/h5/unclustered/IFE_2015_Feb',
            '0035': 'nmx/data/h5/unclustered/IFE_2016_Jun',
            '0036': 'nmx/data/h5/unclustered/IFE_2016_Nov',
            '0037': 'nmx/data/h5/unclustered/IFE_2016_Nov/APZ_threshold_scan',
            '0040': 'nmx/data/h5/unclustered/IFE_2016_Nov/Calibration',
            '0041': 'nmx/data/h5/unclustered/IFE_2016_Nov/Efficiency',
            '0042': 'nmx/data/h5/unclustered/IFE_2016_Nov/Pattern',
            '0043': 'nmx/data/h5/unclustered/IFE_2016_Nov/Scattering'
        }

        fetch_metadata = NmxMetadata()
        self.metadata_object = fetch_metadata.metadata_object


class V20(DefaultInst):
    def __init__(self):
        self.abbreviation = 'V20'

        self.owner = 'Jonas Nilsson'
        self.ownerEmail = 'jonas.nilsson@esss.se'
        self.sourceFolder = 'V20'
        self.orcidOfOwner = '0000-0003-3893-2308'

        self.contactEmail = self.ownerEmail
        self.principalInvestigator = self.owner
        self.userTargetLocation = self.abbreviation
        self.creationLocation = self.abbreviation
        self.keywords = [self.abbreviation]

        self.doi = self.doi_prefix + self.abbreviation
        self.affiliation = 'ESS'
        self.creator = self.owner
        self.publisher = 'ESS'
        self.publicationYear = 2018
        self.title = 'Sample Data from V20'
        self.url = self.url_fragment + self.abbreviation
        self.dataDescription = 'https://github.com/ess-dmsc/ess_file_formats/wiki/V20'
        self.abstract = """This data was collected as part of BrightnESS, funded by the European Union  
                        Framework Programme for Research and Innovation Horizon 2020, under grant 
                        agreement 676548. It consists of test data for the detector."""
        self.resourceType = 'NeXus HDF5 files'
        self.sizeOfArchive = 33.1
        self.numberOfFiles = 11
        self.pidArray = ['string']
        self.authors = ['string']
        self.doiRegisteredSuccessfullyTime = "2018"

        self.scientificMetadata = {
            "chopperFrequency": 14
        }

        self.source_folder_array = {
            '0001': 'v20/2018_01_24'
        }

        self.proposal = '2018ESS1'


class Hzb(DefaultInst):
    def __init__(self):
        self.abbreviation = 'HZB'


class Ife(DefaultInst):
    def __init__(self):
        self.abbreviation = 'IFE'


class Ess(DefaultInst):
    def __init__(self):
        self.abbreviation = 'ESS'


if __name__ == '__main__':
    sonde = Instrument.factory('sonde')
    print(sonde.inst)


class Multiblade(DefaultInst):

    def __init__(self):
        self.abbreviation = 'MB'

        self.owner = 'Francesco Piscitelli'
        self.ownerEmail = 'Francesco.Piscitelli@esss.se'
        self.sourceFolder = 'multiblade/data/brightness/2017_06_BNC_MB16T_ElectronicsTests/DATA'
        self.orcidOfOwner = '0000-0002-0325-4407'
        self.contactEmail = self.ownerEmail
        self.principalInvestigator = self.owner
        self.userTargetLocation = self.abbreviation
        self.creationLocation = self.abbreviation
        self.keywords = [self.abbreviation]

        self.doi = self.doi_prefix + self.abbreviation
        self.creator = self.owner
        self.title = 'Sample Data from Multiblade'
        self.url = self.url_fragment + self.abbreviation
        self.dataDescription = 'https://github.com/ess-dmsc/ess_file_formats/wiki/Zaba'
        self.abstract = """This data was collected as part of BrightnESS, funded by the European Union 
                        Framework Programme for Research and Innovation Horizon 2020, under grant 
                        agreement 676548. It consists of test data for the detector."""
        self.resourceType = 'lst1 files'
        self.pidArray = ['string']
        self.authors = [self.creator]
        self.scientificMetadata = {
            'id': 3
        }
        self.proposal = '2018ESS1'

        self.source_folder_array = {
            '0001': 'multiblade/data/brightness/2016_12_STF_MB15_GammaSensitivity/20161210_gammaSensData',
            '0002': 'multiblade/data/brightness/2017_04_STF_MB15_FastNeutronSensitivity/data_FastNeutron',
            '0003': 'multiblade/data/brightness/2017_06_BNC_MB16T_ElectronicsTests/DATA',
            '0004': 'multiblade/data/brightness/2017_06_BNC_MB16T_ElectronicsTests/DATA_011_images',
            '0005': 'multiblade/data/brightness/2017_06_BNC_MB16T_ElectronicsTests/prove0620',
            '0006': 'multiblade/data/brightness/2017_06_BNC_MB16T_ElectronicsTests/prove0621',
            '0007': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/02_1_provaFirmware',
            '0008': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_10_F_V_test',
            '0009': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_11_G_plexi_test',
            '0010': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_1_provaFirmware',
            '0011': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_2_A_Ni',
            '0012': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_3_B_DirectBeamTests',
            '0013': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_4_B_DirectBeam',
            '0014': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_5_C_DirectBeam_5mmAl',
            '0015': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_6_D_Ir_align',
            '0016': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_7_E_Ir_collimated',
            '0017': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_8_E_Ir_slit',
            '0018': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_9_E_Ir_test',
            '0019': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03N_12_G_plexi',
            '0020': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_10_I2_Si_divergent',
            '0021': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_11_L_FeSi_test',
            '0022': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_1_E_Ir_test',
            '0023': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_2_E1_Ir_collimated',
            '0024': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_3_H_Si_test',
            '0025': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_4_H_Si_collimated',
            '0026': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_5_H1_Si_collimated_HVtests',
            '0027': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_6_I_FeSi_test',
            '0028': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_7_I_FeSi_divergent',
            '0029': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_8_I1_FeSi_divergent_magnet',
            '0030': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_9_I2_Si_divergent_test',
            '0031': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04N_12_L_FeSi_collimated_OffSpec',
            '0032': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_10_P_mask',
            '0033': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_11_Q_Si_divergent_highQ_test',
            '0034': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_1_M_FeSi_collimated_magnet_test',
            '0035': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_2_M_FeSi_collimated_magnet',
            '0036': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_3_N_ResW_test',
            '0037': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_4_N_ResW',
            '0038': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_5_N1_ResW_longRun',
            '0039': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_6_O_PosStrip_test',
            '0040': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_7_O_PosStrip_linkN1',
            '0041': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_8_O1_ResStrip',
            '0042': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_9_P_mask_test',
            '0043': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05N_12_Q_Si_divergent_highQ',
            '0044': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05N_13_Q_Si_divergent_highQ_BeamOff',
            '0045': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/06_1_R_Efficiency_50Hz_test',
            '0046': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/06_2_R_Efficiency_50Hz',
            '0047': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/06_3_R12_Efficiency_25Hz_test',
            '0048': 'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/06_4_R2_Efficiency_25Hz'
        }

        fetch_metadata = MultibladeMetadata()
        self.metadata_object = fetch_metadata.metadata_object


class Sonde(DefaultInst):

    def __init__(self):
        self.abbreviation = 'SONDE'

        self.owner = 'Ramsey Al Jebali'
        self.ownerEmail = 'ramsey.aljebali@esss.se'
        self.sourceFolder = 'sonde/IFE_june_2018/data/S13'
        self.orcidOfOwner = '0000-0000-0000-0000'
        self.contactEmail = self.ownerEmail
        self.principalInvestigator = self.owner
        self.userTargetLocation = self.abbreviation
        self.creationLocation = self.abbreviation
        self.keywords = [self.abbreviation, 'IFE']

        self.doi = self.doi_prefix + self.abbreviation
        self.creator = self.owner
        self.title = 'Sample Data from SONDE'
        self.url = self.url_fragment + self.abbreviation
        self.dataDescription = 'https://github.com/ess-dmsc/ess_file_formats/wiki/SONDE'
        self.abstract = """This data was collected as part of BrightnESS, funded by the European Union 
                        Framework Programme for Research and Innovation Horizon 2020, under grant 
                        agreement 676548. It consists of test data for the detector."""
        self.resourceType = 'Comma Separated Variable (csv) files'
        self.pidArray = ['string']
        self.authors = [self.creator]
        self.doiRegisteredSuccessfullyTime = "2018"
        self.scientificMetadata = {
            'id': 3
        }
        self.proposal = '2018ESS2'

        self.source_folder_array = {
            '0001': 'sonde/IFE_june_2018/data/S1',
            '0002': 'sonde/IFE_june_2018/data/S2',
            '0003': 'sonde/IFE_june_2018/data/S5',
            '0004': 'sonde/IFE_june_2018/data/S6',
            '0005': 'sonde/IFE_june_2018/data/S8',
            '0006': 'sonde/IFE_june_2018/data/S15',
            '0007': 'sonde/IFE_june_2018/data/S11',
            '0008': 'sonde/IFE_june_2018/data/S12',
            '0009': 'sonde/IFE_june_2018/data/S16',
            '0010': 'sonde/IFE_june_2018/data/S14',
            '0011': 'sonde/IFE_june_2018/data/S9',
            '0012': 'sonde/IFE_june_2018/data/S3',
            '0013': 'sonde/IFE_june_2018/data/S13',
            '0014': 'sonde/IFE_june_2018/data/S4',
            '0015': 'sonde/IFE_june_2018/data/S17',
            '0016': 'sonde/IFE_june_2018/data/S7',
            '0017': 'sonde/IFE_june_2018/data/S10',
            '0018': 'sonde/IFE_june_2018/data/temp/t50',
            '0019': 'sonde/IFE_oct_2017/from_EFU_PC/EFU_data',
            '0020': 'sonde/IFE_oct_2017/from_lenovo_laptop/gamma/test_saved_data',
            '0021': 'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/CZTCam',
            '0022': 'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/Default',
            '0023': 'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/Galao-IDE3380_SIPHRA',
            '0024': 'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/Galao-IDE3380_SIPHRA/reg_conf',
            '0025': 'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/Galao-VATA64HDR16',
            '0026': 'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/GammaProcessor',
            '0027': 'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/INX-500',
            '0028': 'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/ROSMAP-MP',
            '0029': 'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/XCS-1000',
            '0030': 'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/logs'
        }
        fetch_metadata = SondeMetadata()
        self.metadata_object = fetch_metadata.metadata_object
