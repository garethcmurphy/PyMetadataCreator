#!/usr/bin/env python3
import datetime
import glob
import json
import os
import re
import socket

from sortedcontainers import SortedDict

from Base64Im import Base64Im
from dataset import Dataset
from dataset import PublishedData
from instrument import Instrument
from lifecycle import LifeCycle
from orig import Orig


class FilesInfo:
    def __init__(self):
        self.files = []
        self.file_number = 22
        self.experiment_date_time = "2017"
        self.total_file_size = 12345654
        self.source_folder = 'source_folder'
        self.base_name = 'base_name'
        self.file_names = []
        self.file_list = []

    @staticmethod
    def get_files(my_dir):
        files = glob.glob(my_dir + '/**.*', recursive=True)
        # print(my_dir)
        # print(files)

        return files

    def extract_file_list(self, source_folder):
        file_number = 0
        total_file_size = 0
        self.file_names = self.get_files(source_folder)
        print(self.file_names[0])
        print('Fetching stat.ctime on all files, n=', len(self.file_names))
        if not self.file_names:
            print("filename empty")
        for file in self.file_names:
            file_number += 1
            longname = file

            stat_info = os.stat(longname)
            rel_path = longname.replace('/users/detector', '/static')
            file_size = stat_info.st_size
            experiment_date_time = stat_info.st_ctime
            ts = int(experiment_date_time)

            experiment_date_time = str(datetime.datetime.fromtimestamp(ts))
            total_file_size += file_size
            file_entry = {
                "path": rel_path,
                "size": file_size,
                "time": experiment_date_time,
                "chk": "string",
                "uid": "string",
                "gid": "string",
                "perm": "string"
            }
            if file_number < 35000:
                self.file_list.append(file_entry)
            self.experiment_date_time = experiment_date_time
            self.file_number = file_number
            self.total_file_size = total_file_size
            self.source_folder = source_folder
        print(self.file_number)
