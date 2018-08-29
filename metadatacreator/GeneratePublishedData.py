#!/usr/bin/env python3
import datetime
import glob
import json
import os
import re
import socket
import sys

from sortedcontainers import SortedDict

from dataset import PublishedData
from instrument import Instrument


class GeneratePublishedData:
    def __init__(self):
        self.mydir = "./data/experiments"
        #        self.mydir = "./static"
        self.year_month_regex = '20[0-9]{2}_[0-1][0-9]'
        self.hostname = socket.gethostname()
        self.filenames = []
        self.file_list = []
        if self.hostname == 'login.esss.dk':
            # self.mydir = "/users/detector/experiments/multiblade/data/brightness"
            self.mydir = "/users/detector/experiments"

    def generate(self):

        data_sets = SortedDict()
        experiments = ['sonde', 'nmx', 'multigrid', 'multiblade']
        experiment_date_time = str(datetime.datetime(2018, 1, 1))

        for i in range(0, 4):
            print(i)
            experiment = experiments[i]
            print(experiment)

            d = PublishedData()
            new_inst = Instrument()
            inst = new_inst.factory(experiment)
            my_data_set = d.published_data
            print(inst.abbreviation)
            my_data_set["doi"] = '10.17199/BRIGHTNESS/' + inst.abbreviation + str(1).zfill(4)
            print(my_data_set["doi"])
            self.file_list = []

            source_folder = self.mydir + '/' + inst.inst["sourceFolder"]
            print('gm source  folder ', source_folder)
            self.filenames = self.get_files(source_folder)
            print(self.filenames)

            experiment_date_time, total_file_size = self.extract_file_list(experiment_date_time)

            my_data_set["doi"] = str(my_data_set["doi"])
            my_data_set["affiliation"] = inst.affiliation
            my_data_set["publisher"] = inst.publisher
            my_data_set["creator"] = inst.creator
            my_data_set["title"] = inst.title
            my_data_set["publicationYear"] = inst.publicationYear
            my_data_set["publisher"] = inst.publisher
            my_data_set["resourceType"] = inst.resourceType
            my_data_set["abstract"] = inst.abstract
            my_data_set["url"] = inst.url

            scicat_entries = {"published_data": my_data_set}
            data_sets["orig" + experiment_date_time + str(i).zfill(5)] = scicat_entries

        json.dump(data_sets, sys.stdout, indent=2)

        with open('published_data.json', 'w') as f:
            json.dump(data_sets, f, ensure_ascii=False, indent=2)

    def extract_file_list(self, experiment_date_time):
        filenum = 0
        total_file_size = 0
        for file in self.filenames:
            filenum += 1
            longname = file

            stat_info = os.stat(longname)
            # rel_path = longname.replace('./data', '/static')
            rel_path = longname.replace('/users/detector', '/static')
            file_size = stat_info.st_size
            experiment_date_time = stat_info.st_ctime
            print(experiment_date_time)
            ts = int(experiment_date_time)

            experiment_date_time = str(datetime.datetime.fromtimestamp(ts))
            print(experiment_date_time)
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
            if filenum < 50:
                self.file_list.append(file_entry)
        return experiment_date_time, total_file_size

    def get_date_information(self, basename, dirpath):
        year_month = "2018_01"
        search_result = re.search(self.year_month_regex, dirpath)
        if search_result:
            year_month = search_result.group(0)
        # print('gm',year_month)
        year = year_month[0:4]
        month = year_month[5:7]
        day = 1
        if re.match('[0-3][0-9]', basename):
            day1 = int(basename[0:2])
            if day1 >= 1:
                day = int(basename[0:2])
        print(year, month, day)
        data_date = datetime.datetime(int(year), int(month), int(day))
        experiment_date_time = data_date.isoformat()
        return experiment_date_time

    @staticmethod
    def get_files(my_dir):

        files = glob.glob(my_dir + '/**.*', recursive=True)

        return files


if __name__ == '__main__':
    g = GeneratePublishedData()
    g.generate()
