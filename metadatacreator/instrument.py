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
            'sonde/IFE_june_2018/data/S5',
            'sonde/IFE_june_2018/data/S12',
            'sonde/IFE_june_2018/data/S2',
            'sonde/IFE_june_2018/data/S8',
            'sonde/IFE_june_2018/data/S15',
            'sonde/IFE_june_2018/data/S11',
            'sonde/IFE_june_2018/data/S6',
            'sonde/IFE_june_2018/data/S16',
            'sonde/IFE_june_2018/data/S14',
            'sonde/IFE_june_2018/data/S9',
            'sonde/IFE_june_2018/data/S3',
            'sonde/IFE_june_2018/data/S13',
            'sonde/IFE_june_2018/data/S4',
            'sonde/IFE_june_2018/data/S17',
            'sonde/IFE_june_2018/data/S7',
            'sonde/IFE_june_2018/data/S10',
            'sonde/IFE_june_2018/data/temp/t50',
            'sonde/IFE_oct_2017/from_EFU_PC/EFU_data',
            'sonde/IFE_oct_2017/from_lenovo_laptop/gamma/test_saved_data',
            'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/CZTCam',
            'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/Default',
            'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/Galao-IDE3380_SIPHRA',
            'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/Galao-IDE3380_SIPHRA/reg_conf',
            'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/Galao-VATA64HDR16',
            'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/GammaProcessor',
            'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/INX-500',
            'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/ROSMAP-MP',
            'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/conf/XCS-1000',
            'sonde/IFE_oct_2017/from_lenovo_laptop/IDEASTestbench_BETA_V0_24-x86-ALL/logs'
        ]

        self.inst = {'owner': 'Ramsey Al Jebali',
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
            'multiblade/data/brightness/2016_12_STF_MB15_GammaSensitivity/20161210_gammaSensData',
            'multiblade/data/brightness/2017_04_STF_MB15_FastNeutronSensitivity/data_FastNeutron',
            'multiblade/data/brightness/2017_06_BNC_MB16T_ElectronicsTests/DATA',
            'multiblade/data/brightness/2017_06_BNC_MB16T_ElectronicsTests/DATA_011_images',
            'multiblade/data/brightness/2017_06_BNC_MB16T_ElectronicsTests/prove0620',
            'multiblade/data/brightness/2017_06_BNC_MB16T_ElectronicsTests/prove0621',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/02_1_provaFirmware',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_10_F_V_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_11_G_plexi_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_1_provaFirmware',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_2_A_Ni',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_3_B_DirectBeamTests',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_4_B_DirectBeam',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_5_C_DirectBeam_5mmAl',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_6_D_Ir_align',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_7_E_Ir_collimated',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_8_E_Ir_slit',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03_9_E_Ir_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/03N_12_G_plexi',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_10_I2_Si_divergent',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_11_L_FeSi_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_1_E_Ir_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_2_E1_Ir_collimated',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_3_H_Si_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_4_H_Si_collimated',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_5_H1_Si_collimated_HVtests',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_6_I_FeSi_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_7_I_FeSi_divergent',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_8_I1_FeSi_divergent_magnet',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04_9_I2_Si_divergent_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/04N_12_L_FeSi_collimated_OffSpec',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_10_P_mask',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_11_Q_Si_divergent_highQ_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_1_M_FeSi_collimated_magnet_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_2_M_FeSi_collimated_magnet',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_3_N_ResW_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_4_N_ResW',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_5_N1_ResW_longRun',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_6_O_PosStrip_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_7_O_PosStrip_linkN1',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_8_O1_ResStrip',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05_9_P_mask_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05N_12_Q_Si_divergent_highQ',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/05N_13_Q_Si_divergent_highQ_BeamOff',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/06_1_R_Efficiency_50Hz_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/06_2_R_Efficiency_50Hz',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/06_3_R12_Efficiency_25Hz_test',
            'multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/06_4_R2_Efficiency_25Hz'
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
