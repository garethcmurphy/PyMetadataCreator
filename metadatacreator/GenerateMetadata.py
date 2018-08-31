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
from orig import Orig


class FilesInfo:
    def __init__(self):
        self.files = []
        self.file_number = 22
        self.experiment_date_time = "2017"
        self.total_file_size = 12345654
        self.source_folder = 'source_folder'
        self.base_name = 'base_name'


class GenerateMetadata:
    def __init__(self):
        self.global_file_number = 0
        self.my_directory = "./data/experiments"
        #        self.mydir = "./static"
        self.year_month_regex = '20[0-9]{2}_[0-1][0-9]'
        self.hostname = socket.gethostname()
        self.file_names = []
        self.file_list = []
        if self.hostname == 'login.esss.dk':
            # self.mydir = "/users/detector/experiments/multiblade/data/brightness"
            self.my_directory = "/users/detector/experiments"

    def generate(self):

        data_sets = SortedDict()
        experiments = [
            'v20',
            'sonde',
            'nmx',
            'multiblade',
            'multigrid',
        ]

        for i in range(0, 5):
            print(i)
            experiment = experiments[i]
            print(experiment)

            new_inst = Instrument()
            inst = new_inst.factory(experiment)

            data_set_num = 0
            for source_folder_fragment in inst.source_folder_array:
                source_folder = self.my_directory + '/' + source_folder_fragment
                data_set_num = data_set_num + 1
                self.file_list = []
                file_info = self.extract_file_list(source_folder)
                self.global_file_number += file_info.file_number
                my_data_set = self.get_dataset(inst, data_set_num, file_info)

                my_orig = self.get_orig_blocks(my_data_set, file_info)

                my_published = self.get_published_data(inst, my_data_set, file_info)

                scicat_entries = {
                    "dataset": my_data_set,
                    "orig": my_orig,
                    "published": my_published
                }
                data_sets[
                    "orig" + file_info.experiment_date_time + str(i).zfill(5) + str(data_set_num).zfill(
                        5)] = scicat_entries
        # json.dump(data_sets, sys.stdout, indent=2)
        print("Files processed =", self.global_file_number)
        with open('test_new_metadata.json', 'w') as f:
            json.dump(data_sets, f, ensure_ascii=False, indent=2)

    @staticmethod
    def get_dataset(inst, data_set_number, files_info):
        d = Dataset()
        my_data_set = d.dataset
        print(inst.abbreviation)
        my_data_set.update(inst.inst)
        my_data_set["pid"] = '10.17199/BRIGHTNESS/' + inst.abbreviation + str(data_set_number).zfill(4)
        print(my_data_set["pid"])
        my_data_set["size"] = files_info.total_file_size
        my_data_set["packedSize"] = files_info.total_file_size
        my_data_set["creationTime"] = files_info.experiment_date_time
        my_data_set["endTime"] = files_info.experiment_date_time
        my_data_set["createdAt"] = files_info.experiment_date_time
        my_data_set["updatedAt"] = files_info.experiment_date_time
        my_data_set["doi"] = str(my_data_set["pid"])
        my_data_set["sourceFolder"] = files_info.source_folder
        my_data_set["scientificMetadata"] = inst.scientificMetadata
        my_data_set["proposalId"] = inst.proposal

        return my_data_set

    def get_orig_blocks(self, my_data_set, file_info):
        orig = Orig()
        my_orig = orig.orig
        my_orig["datasetId"] = str(my_data_set["pid"])
        my_orig["dataFileList"] = self.file_list
        my_orig["size"] = file_info.total_file_size
        my_orig["createdAt"] = file_info.experiment_date_time
        my_orig["updatedAt"] = file_info.experiment_date_time
        return my_orig

    @staticmethod
    def get_published_data(inst, my_data_set, file_info):
        published = PublishedData()
        my_published = published.published_data
        my_published["doi"] = str(my_data_set["doi"])
        my_published["affiliation"] = inst.affiliation
        my_published["publisher"] = inst.publisher
        my_published["creator"] = inst.creator
        my_published["title"] = inst.title
        my_published["publicationYear"] = inst.publicationYear
        my_published["publisher"] = inst.publisher
        my_published["resourceType"] = inst.resourceType
        my_published["abstract"] = inst.abstract
        im = Base64Im()
        my_published["thumbnail"] = im.im
        my_published["url"] = inst.url
        my_published["sizeOfArchive"] = file_info.total_file_size
        my_published["numberOfFiles"] = file_info.file_number
        return my_published

    def extract_file_list(self, source_folder):
        files_info = FilesInfo()
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
            # rel_path = longname.replace('./data', '/static')
            rel_path = longname.replace('/users/detector', '/static')
            file_size = stat_info.st_size
            experiment_date_time = stat_info.st_ctime
            # print(experiment_date_time)
            ts = int(experiment_date_time)

            experiment_date_time = str(datetime.datetime.fromtimestamp(ts))
            # print(experiment_date_time)
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
            files_info.experiment_date_time = experiment_date_time
            files_info.file_number = file_number
            files_info.total_file_size = total_file_size
            files_info.source_folder = source_folder
        print(files_info.file_number)
        return files_info

    def get_date_information(self, basename, directory_path):
        year_month = "2018_01"
        search_result = re.search(self.year_month_regex, directory_path)
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
        # print(my_dir)
        # print(files)

        return files


if __name__ == '__main__':
    g = GenerateMetadata()
    g.generate()
