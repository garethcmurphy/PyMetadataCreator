#!/usr/bin/env python3
"""import metadata from elog for sonde"""
import json
from urllib.parse import urljoin

import dateutil.parser as parser
from dateutil import tz
import requests
from bs4 import BeautifulSoup

from extract_table import ExtractTable


class SondeImport:
    """import metadata from elog for sonde"""
    def __init__(self):
        url = "https://stf02.nuclear.lu.se/SoNDe+Testbeams/"

        soup = self.scrape_url(url)

        data = []
        table = soup.find("table", {"class": "listframe"})
        # print(table)

        rows = table.find_all(['tr'])
        # print("gm")
        # print(rows[3])

        master_dict = {}
        extract_table = ExtractTable.ExtractTable()
        num = 1
        for row in rows:
            num = num + 1
            first = row.find('a')
            sub_page_message = "null"
            print(num, first)
            if num > 2:
                src = urljoin(url, first["href"])
                sub_page_soup = self.scrape_url(src)
                sub_page_message = sub_page_soup.find("pre").find(text=True)
                # print(sub_page_message)
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])  # Get rid of empty values
            # print(cols)
            my_dict = {}
            my_id = "null"
            if cols:
                my_dict["elog_id"] = cols[0]
                my_dict["elog_url"] = src
                date = parser.parse(cols[1], yearfirst=True)
                my_dict["date"] = date.replace(tzinfo=tz.tzlocal()).isoformat()
                my_dict["author"] = cols[2]
                my_dict["beamline"] = cols[3]
                my_dict["type"] = cols[4]
                my_dict["category"] = cols[5]
                my_id = cols[0]
                my_dict["run"] = cols[6]
                my_dict["subject"] = cols[7]

                extracted_table = extract_table.get_table(sub_page_message)
                my_dict.update(extracted_table)
            if my_id != "null":
                master_dict[my_id] = my_dict

        j = json.dumps(master_dict, indent=2)
        print(j)
        with open('sonde.json', 'w') as f:
            f.write(j)

    def scrape_url(self, url):
        """scrape from URL"""
        r = requests.get(url)
        sonde_page = r.text
        soup = BeautifulSoup(sonde_page, "lxml")
        return soup


if __name__ == '__main__':
    sonde = SondeImport()
