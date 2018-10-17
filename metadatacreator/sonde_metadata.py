#!/usr/bin/env python3
import json


class SondeMetadata:

    def __init__(self):
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
        with open('sonde.json') as json_data:
            self.metadata_object = json.load(json_data)
            # self.json_stuff = json.load(json_data)
            # TODO get the actual keys with property value and correct key


if __name__ == '__main__':
    nmx = SondeMetadata()
    print(nmx.metadata_object)
