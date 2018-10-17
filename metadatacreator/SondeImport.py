#!/usr/bin/env python3
import json
from collections import OrderedDict

from bs4 import BeautifulSoup


class SondeImport:

    def __init__(self):
        html_data = """
        <table>
          <tr>
            <td>Card balance</td>
            <td>$18.30</td>
          </tr>
          <tr>
            <td>Card name</td>
            <td>NAMEn</td>
          </tr>
          <tr>
            <td>Account holder</td>
            <td>NAME</td>
          </tr>
          <tr>
            <td>Card number</td>
            <td>1234</td>
          </tr>
          <tr>
            <td>Status</td>
            <td>Active</td>
          </tr>
        </table>
        """

        table_data = [[cell.text for cell in row("td")]
                      for row in BeautifulSoup(html_data, features="html.parser")("tr")]

        print(json.dumps(OrderedDict(table_data, indent=2)))


if __name__ == '__main__':
    sonde = SondeImport()
