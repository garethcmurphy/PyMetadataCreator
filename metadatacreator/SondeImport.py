#!/usr/bin/env python3
import json
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class SondeImport:
    def __init__(self):
        url = "https://stf02.nuclear.lu.se/SoNDe+Testbeams/"
        r = requests.get(url)
        sonde_page = r.text

        soup = BeautifulSoup(sonde_page, "lxml")

        data = []
        table = soup.find("table", {"class": "listframe"})
        # print(table)

        rows = table.find_all(['tr'])
        # print("gm")
        # print(rows[3])

        master_dict = {}
        num = 1
        for row in rows:
            num = num + 1
            first = row.find('a')
            print(num, first)
            if num > 2:
                src = urljoin(url, first["href"])
                print(src)
                sub_page = requests.get(src)
                sub_page_soup = BeautifulSoup(sub_page.text, "lxml")
                sub_page_message = sub_page_soup.find("pre").find(text=True)
                print(sub_page_message)
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])  # Get rid of empty values
            # print(cols)
            my_dict = {}
            my_id = "null"
            if cols:
                my_dict["id"] = cols[0]
                my_dict["date"] = cols[1]
                my_dict["author"] = cols[2]
                my_dict["beamline"] = cols[3]
                my_dict["type"] = cols[4]
                my_dict["category"] = cols[5]
                my_id = cols[0]
                my_dict["run"] = cols[6]
                my_dict["subject"] = cols[7]
                my_dict["message"] = sub_page_message
            if my_id != "null":
                master_dict[my_id] = my_dict

        j=json.dumps(master_dict, indent=2)
        print(j)
        with open('sonde.json', 'w') as f:
            f.write(j)


if __name__ == '__main__':
    sonde = SondeImport()
