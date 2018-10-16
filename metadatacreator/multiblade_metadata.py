class MultibladeMetadata:
    metadata_object = {
        '0001': {"wavelength": 2, 'comment': 'xxx'},
        '0011': {'tag': '03_2_A_Ni',
                 'comment': 'reflected Beam Ni: Measurements of Ni -> magnetic (double fringe)'},
        '0012': {'tag': '03_3_B_DirectBeam', 'comment': 'direct Beam Measurements',
                 'current Total microA': '1',
                 'time ': '2 minutes',
                 'fileNumber': '43',
                 'start': '167/185',
                 'stop': '166',
                 },
        '0012': {
            'tag': '03_4_B_DirectBeamTests',
            'comment': 'reflected Beam Ni: Measurements of Ni -> magnetic (double fringe)'
        },
        '0014': {
            'tag': '03_5_C_DirectBeam_5mmAl',
            'comment': 'direct Beam, 5 minutes Al plate in front of the window',
            'time': '2 minutes',
            'start': '167/2.82',
            'stop': '166.6/25.92',
            'start1': '166.05/1.63',
            'stop1': '166/25.18',
        },
        '0015': {'tag': '03_6_D_Ir_align',
                 'comment': 'sample iridium',
                 'comment1': 'centering 122 config iridium Hz fixed = -1.7'
                 },
        '0016': {'tag': '03_7_E_Ir_collimated',
                 'comment': 'sample iridium',
                 'current start': '167 / 0.47',
                 'current stop': '168 / 15',
                 },
        '0017': {'tag': '03_8_E_Ir_slit',
                 'comment': 'xxx'},
        '0018': {'tag': '03_9_E_Ir_test',
                 'comment': 'change the detector position from 0-> 10',
                 'comment1': 'doesnt change -> its the detector',
                 'comment2': 'beam turned off -> NO visible anymore',
                 },
        '0019': {'tag': '03N_12_G_plexi',
                 'comment': 'plexiglass',
                 'comment1': 'uniformity information: all the active area is involved because of the scattering ',
                 ' thickness': ' 4 mm'},
        '0020': {
            'tag': '04_10_I2_Si_divergent',
            'comment': 'xxx'},
        '0021': {'tag': '04_11_L_FeSi_test',
                 'comment': 'sample SM off specular',
                 'P': '0',
                 'Hz': '1.8',
                 'Hx': '100',
                 'Phi': 'scan',
                 'slit s1': '1.2',
                 'slit s2': '0.5',
                 'slit s3': '17.3',
                 },
        '0022': {'tag': '04_1_E_Ir_test',
                 'comment': 'xxx',
                 },
        '0023': {
            'tag': '04_2_E1_Ir_collimated',
            'comment': 'xxx',
        },
        '0024': {'tag': '04_3_H_Si_test',
                 'comment': 'sample silicon',
                 },
        '0025': {'tag': '04_4_H_Si_collimated',
                 'comment': 'sample silicon collimated beam'},
        '0026': {
            'tag': '04_5_H1_Si_collimated_HVtests',
            'comment': 'xxx'},
        '0027': {'tag': '04_6_I_FeSi_test',
                 'comment': 'xxx'},
        '0028': {
            'tag': '04_7_I_FeSi_divergent',
            'comment': 'sample super mirror divergent'},
        '0029': {
            'tag': '04_8_I1_FeSi_divergent_magnet',
            'comment': 'magnet added to converge the Fex and reflection. We expect less H-specular'},
        '0030': {
            'tag': '04_9_I2_Si_divergent_test',
            'comment': 'sample silicon divergent',
            'Hz': '-6.9',
            'Hx': '100',
            'phi': 'scan',
            'comment1': 'phi aligment and slide 4 low=-1.5',
        },
        '0031': {
            'tag': '04N_12_L_FeSi_collimated_OffSpec',
            'comment': 'Off Specular (FeSi) m=3.8 collimated beam'
        },
        '0032': {'tag': '05_10_P_mask',
                 'comment': 'xxx'},
        '0033': {
            'tag': '05_11_Q_Si_divergent_highQ_test',
            'comment': 'xxx'},
        '0034': {
            'tag': '05_1_M_FeSi_collimated_magnet_test',
            'comment': 'xxx'},
        '0035': {
            'tag': '05_2_M_FeSi_collimated_magnet',
            'comment': 'xxx'},
        '0036': {'tag': '05_3_N_ResW_test', 'comment': 'xxx'},
        '0037': {'tag': '05_4_N_ResW', 'comment': 'xxx'},
        '0038': {'tag': '05_5_N1_ResW_longRun', 'comment': 'xxx'},
        '0039': {'tag': '05_6_O_PosStrip_test', 'comment': 'xxx'},
        '0040': {
            'tag': '05_7_O_PosStrip_linkN1', 'comment': 'xxx'},
        '0041': {'tag': '05_8_O1_ResStrip', 'comment': 'xxx'},
        '0042': {'tag': '05_9_P_mask_test',
                 'comment': 'resolution mask',
                 'comment2': '''first direct beam on detector. To have a wider beam we put the 
                 supermirror with the magnet and divergent beam. We use the ESS mask''',
                 },
        '0043': {
            'tag': '05N_12_Q_Si_divergent_highQ',
            'comment': 'xxx'},
        '0044': {
            'tag': '05N_13_Q_Si_divergent_highQ_BeamOff',
            'comment': 'xxx'},
        '0045': {
            'tag': '06_1_R_Efficiency_50Hz_test',
            'comment': '''Comparison MB vs 3He, we use the direct beam. We want to see the footprint with the MB, 
            to be sure we have the same in both detectors. Then we can calculate the efficiency from the comparison'''},
        '0046': {
            'tag': '06_2_R_Efficiency_50Hz',
            'comment': 'xxx'},
        '0047': {
            'tag': '06_3_R12_Efficiency_25Hz_test',
            'comment': 'xxx'},
        '0048': {
            'tag': '06_4_R2_Efficiency_25Hz'
        }
    }
