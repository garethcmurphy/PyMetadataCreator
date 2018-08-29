#!/usr/bin/env python3
import datetime
import glob
import json
import os
import re
import socket
import sys

from sortedcontainers import SortedDict

from dataset import Dataset
from instrument import Instrument
from orig import Orig


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
        i = 0
        experiments = ['sonde', 'nmx', 'multigrid', 'multiblade']
        experiment_date_time = str(datetime.datetime(2018, 1, 1))

        for i in range(0, 4):
            print(i)
            experiment = experiments[i]
            print(experiment)

            d = Dataset()
            new_inst = Instrument()
            inst = new_inst.factory(experiment)
            my_data_set = d.dataset
            print(inst.abbreviation)
            my_data_set.update(inst.inst)
            my_data_set["pid"] = '10.17199/BRIGHTNESS/' + inst.abbreviation + str(1).zfill(4)
            print(my_data_set["pid"])
            self.file_list = []

            sourceFolder = self.mydir + '/' + inst.inst["sourceFolder"]
            print('gm source  folder ', sourceFolder)
            self.filenames = self.get_files(sourceFolder)
            basename = 'test_sci_met'
            basename = 'test_base_name'
            print(self.filenames)

            experiment_date_time, total_file_size = self.extract_file_list(experiment_date_time)

            my_data_set["size"] = total_file_size
            my_data_set["packedSize"] = total_file_size
            my_data_set["creationTime"] = experiment_date_time
            my_data_set["endTime"] = experiment_date_time
            my_data_set["createdAt"] = experiment_date_time
            my_data_set["updatedAt"] = experiment_date_time
            my_data_set["doi"] = str(my_data_set["pid"])
            scientific_metadata = {
                "identifier": basename
            }
            my_data_set["scientificMetadata"] = scientific_metadata
            orig = Orig()
            my_orig = orig.orig
            my_orig["datasetId"] = str(my_data_set["pid"])
            my_orig["dataFileList"] = self.file_list
            my_orig["size"] = total_file_size
            my_orig["createdAt"] = experiment_date_time
            my_orig["updatedAt"] = experiment_date_time

            scicat_entries = {"dataset": my_data_set, "orig": my_orig}
            data_sets["orig" + experiment_date_time + str(i).zfill(5)] = scicat_entries

        json.dump(data_sets, sys.stdout, indent=2)

        with open('test_new_metadata.json', 'w') as f:
            json.dump(data_sets, f, ensure_ascii=False, indent=2)

    def extract_file_list(self, experiment_date_time):
        filenum = 0
        total_file_size = 0
        for file in self.filenames:
            filenum += 1
            longname = file

            stat_info = os.stat(longname)
            rel_path = longname.replace('./data', '/static')
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

    def get_files(self, my_dir):

        files = glob.glob(my_dir + '/**.*', recursive=True)

        return files


if __name__ == '__main__':
    g = GenerateMetadata()
    g.generate()
