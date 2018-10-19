#!/usr/bin/env python3
import json
import re
import io


class ExtractTable:
    def __init__(self):
        self.x = 'begin search'

    @staticmethod
    def get_table(example):
        stri = io.StringIO(example)
        my_table = {}
        comments = ""
        for line in stri:
            nl = line
            # print(nl)
            p = re.compile('(?:> )*((?:(?!\.\.).)+)\.{2,}(.+)\s*\n')
            result = p.search(nl)
            print(result)
            if result:
                match = result.group()
                begin_position = match.find('..')
                key = match[:begin_position]
                end_position = match.rfind('..')
                val = match[end_position + 2:]
                val = val.strip()
                key_for_mongo = key.replace('.', '_')
                my_table[key_for_mongo] = val
            else:
                comments = comments + (nl.strip())
            my_table["comments"] = comments

        return (my_table)


if __name__ == '__main__':
    extract = ExtractTable()
    example_strings = [
        "To test the gamma sensitivity of the detector, the beam was turned off and an Cs-137 source was placed in the same position as the beam on the last collimator (see image).\r\nAttached is an image of the setup and 2D plot of the accumulated triggers for all 64 pixels. In the plot we can see that the highest gain pixels are have a higher rate, as \r\nexpected.\r\n\r\nRuntime: 17 min\r\nDistance source to scintillator: 9.5 cm\r\n\r\n----- Settings and configuration ---------\r\nMAPMT..............ZA0250 @ 900 V\r\nSoNDe module.......7053-1-008\r\nSoNDe acqu. mode...ACRO \r\nSoNDe threshold....10\r\nScintillator.......GS20 (plain, polished)\r\nOptical coupling...Dryfit\r\n------------------------------------------\r\n\r\nAttachment 2 shows a heatmap of the integrated 17 minutes triggers, as shown in daquri.",
        "freuieafghuiregfhrei"
    ]
    for example in example_strings:
        my_table = extract.get_table(example)
        print(json.dumps(my_table, indent=2))
