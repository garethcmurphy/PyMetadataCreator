#!/usr/bin/env python3
import pandas as pd


class ExcelImporter:
    def __init__(self):
        self.filename = "/Users/garethmurphy/Documents/multigrid_metadata.xlsx"
        pass

    def read_excel(self) -> object:
        df_out = pd.read_excel(self.filename, index_col=None, header=0)
        # print(df_out)
        print(list(df_out))
        print(df_out)


if __name__ == '__main__':
    ei = ExcelImporter()
    ei.read_excel()
