#!/usr/bin/env python3

import re


class ExtractTable:
    def __init__(self):
        self.example = "To test the gamma sensitivity of the detector, the beam was turned off and an Cs-137 source was placed in the same position as the beam on the last collimator (see image).\r\nAttached is an image of the setup and 2D plot of the accumulated triggers for all 64 pixels. In the plot we can see that the highest gain pixels are have a higher rate, as \r\nexpected.\r\n\r\nRuntime: 17 min\r\nDistance source to scintillator: 9.5 cm\r\n\r\n----- Settings and configuration ---------\r\nMAPMT..............ZA0250 @ 900 V\r\nSoNDe module.......7053-1-008\r\nSoNDe acqu. mode...ACRO \r\nSoNDe threshold....10\r\nScintillator.......GS20 (plain, polished)\r\nOptical coupling...Dryfit\r\n------------------------------------------\r\n\r\nAttachment 2 shows a heatmap of the integrated 17 minutes triggers, as shown in daquri."

    def get_table(self):
        result = re.search('--(.*)--', self.example,  re.MULTILINE)
        print(result)


if __name__ == '__main__':
    extract = ExtractTable()
    extract.get_table()
