#!/usr/bin/env python3
import json
from collections import OrderedDict

from bs4 import BeautifulSoup
import requests


class SondeImport:
    def __init__(self):
        url = "stf02.nuclear.lu.se/SoNDe+Testbeams/"
        r = requests.get("https://" + url)
        sonde_page = r.text

        soup = BeautifulSoup(sonde_page)

        data = []
        table = soup.findAll("table", {"class": "listframe"})
        print(table)

        dats = table.findAll(['td'])
        print(dats)

        # for row in rows:
        #    cols = row.find_all('td')
        #    cols = [ele.text.strip() for ele in cols]
        #    data.append([ele for ele in cols if ele])  # Get rid of empty values


if __name__ == '__main__':
    sonde = SondeImport()
