#!/usr/bin/env python3

from collections import OrderedDict

import simplejson as json
import xlrd

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('20161101_measurements.xlsx')
sh = wb.sheet_by_index(0)

# List to hold dictionaries
metadata_fields_list = []
metadata_fields_object = {}

# Iterate through each row in worksheet and fetch values into dict
for rownum in range(2, sh.nrows):
    metadata_fields = OrderedDict()
    row_values = sh.row_values(rownum)
    key = str(rownum - 1).zfill(4)
    metadata_fields['key'] = key
    metadata_fields['detector'] = row_values[0]
    metadata_fields['purpose'] = row_values[1]
    metadata_fields['F+GEM V'] = row_values[2]
    metadata_fields['Dfield'] = row_values[3]
    metadata_fields['F+D V'] = row_values[4]
    metadata_fields['Config'] = row_values[5]
    metadata_fields['Wavelength[A]'] = row_values[6]
    metadata_fields['Beam'] = row_values[7]
    metadata_fields['AlB03'] = row_values[8]
    metadata_fields['B4C'] = row_values[9]
    metadata_fields['AlB032'] = row_values[10]
    metadata_fields['B4C_2'] = row_values[11]
    metadata_fields['B4C_3'] = row_values[12]
    metadata_fields['B4C sum'] = row_values[13]
    metadata_fields['mask'] = row_values[14]
    metadata_fields['Dfield'] = row_values[15]
    metadata_fields['MCA_s'] = row_values[16]
    metadata_fields['He3'] = row_values[17]
    metadata_fields['He3 s'] = row_values[18]
    metadata_fields['tick'] = row_values[19]
    metadata_fields['runNumber'] = row_values[20]
    metadata_fields['1e3 Hits'] = row_values[21]
    metadata_fields['Chip'] = row_values[22]
    metadata_fields['Zs'] = row_values[23]
    metadata_fields['threshold'] = row_values[24]
    metadata_fields['filename'] = row_values[25]

    metadata_fields_list.append(metadata_fields)
    metadata_fields_object[key] = metadata_fields

# Serialize the list of dicts to JSON
j = json.dumps(metadata_fields_object, indent=2)

# Write to file
with open('nmx.json', 'w') as f:
    f.write(j)
