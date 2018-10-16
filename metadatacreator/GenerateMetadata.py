#!/usr/bin/env python3
import datetime
import json
import re
import socket

from sortedcontainers import SortedDict

from Base64Im import Base64Im
from FilesInfo import FilesInfo
from dataset import Dataset
from dataset import PublishedData
from datasetlifecycle import DatasetLifecycle
from instrument import Instrument
from origdatablocks import OrigDatablocks
import time


class GenerateMetadata:
    def __init__(self):
        self.global_file_number = 0
        self.my_directory = "./data/experiments"
        #        self.mydir = "./static"
        self.year_month_regex = '20[0-9]{2}_[0-1][0-9]'
        self.hostname = socket.gethostname()
        image = Base64Im()
        self.image = image.im

        self.handle_prefix = '20.500.12269'
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
            for key, source_folder_fragment in inst.source_folder_array.items():
                source_folder = self.my_directory + '/' + source_folder_fragment
                if self.hostname == "CI0020036":
                    source_folder = "demo"
                data_set_num = data_set_num + 1
                files_info = FilesInfo()
                files_info.extract_file_list(source_folder)
                self.global_file_number += files_info.file_number

                my_data_set = self.get_dataset(inst, data_set_num, files_info)
                my_orig = self.get_orig_blocks(my_data_set, files_info)
                my_published = self.get_published_data(inst, my_data_set, files_info, key)
                my_lifecycle = self.get_lifecycle(inst, my_data_set, files_info)

                scicat_entries = {
                    "dataset": my_data_set.__dict__,
                    "orig": my_orig.__dict__,
                    "published": my_published.__dict__,
                    "lifecycle": my_lifecycle.__dict__
                }
                data_sets[
                    "orig" + files_info.experiment_date_time + str(i).zfill(5) + str(data_set_num).zfill(
                        5)] = scicat_entries
        print("Files processed =", self.global_file_number)
        with open('test_new_metadata.json', 'w') as f:
            json.dump(data_sets, f, ensure_ascii=False, indent=2)

    def get_dataset(self, inst, data_set_number, files_info):
        my_data_set = Dataset()
        print(inst.abbreviation)
        my_data_set.principalInvestigator = inst.principalInvestigator
        my_data_set.endTime = inst.endTime
        my_data_set.creationLocation = inst.creationLocation
        my_data_set.owner = inst.owner
        my_data_set.ownerEmail = inst.ownerEmail
        my_data_set.orcidOfOwner = inst.orcidOfOwner
        my_data_set.contactEmail = inst.contactEmail

        my_data_set.pid = self.handle_prefix + '/BRIGHTNESS/' + inst.abbreviation + str(data_set_number).zfill(4)
        print(my_data_set.pid)
        my_data_set.size = files_info.total_file_size
        my_data_set.packedSize = files_info.total_file_size
        my_data_set.creationTime = files_info.experiment_date_time
        my_data_set.endTime = files_info.experiment_date_time
        my_data_set.createdAt = files_info.experiment_date_time
        my_data_set.updatedAt = files_info.experiment_date_time
        my_data_set.doi = inst.doi + str(data_set_number).zfill(4)
        my_data_set.sourceFolder = files_info.source_folder
        my_data_set.scientificMetadata = inst.scientificMetadata
        my_data_set.proposalId = inst.proposal
        my_data_set.validationStatus = inst.validationStatus
        my_data_set.keywords = inst.keywords
        my_data_set.description = inst.dataDescription
        my_data_set.userTargetLocation = inst.userTargetLocation
        my_data_set.classification = inst.classification
        my_data_set.license = inst.license
        my_data_set.version = inst.version
        my_data_set.type = inst.type
        my_data_set.ownerGroup = inst.ownerGroup
        my_data_set.accessGroups = inst.accessGroups

        return my_data_set

    @staticmethod
    def get_orig_blocks(my_data_set, file_info):
        my_orig = OrigDatablocks()
        my_orig.datasetId = str(my_data_set.pid)
        my_orig.dataFileList = file_info.file_list
        my_orig.size = file_info.total_file_size
        my_orig.createdAt = file_info.experiment_date_time
        my_orig.updatedAt = file_info.experiment_date_time
        return my_orig

    def get_published_data(self,inst, my_data_set, file_info, key):
        my_published = PublishedData()
        my_published.doi = str(my_data_set.doi)
        my_published.affiliation = inst.affiliation
        my_published.publisher = inst.publisher
        my_published.creator = inst.creator
        my_published.title = inst.title
        my_published.publicationYear = inst.publicationYear
        my_published.publisher = inst.publisher
        my_published.resourceType = inst.resourceType
        my_published.abstract = inst.abstract
        im = Base64Im()
        my_published.thumbnail = self.image
        my_published.url = inst.url + key
        my_published.sizeOfArchive = file_info.total_file_size
        my_published.numberOfFiles = file_info.file_number
        my_published.dataDescription = inst.dataDescription
        my_published.authors = inst.authors
        my_published.pidArray = inst.pidArray
        return my_published

    @staticmethod
    def get_lifecycle(inst, my_data_set, file_info):
        current_date = datetime.datetime.now().isoformat()
        lifecycle = DatasetLifecycle()
        lifecycle.id = str(my_data_set.pid)
        lifecycle.isOnDisk = inst.isOnDisk
        lifecycle.isOnTape = inst.isOnTape
        lifecycle.archivable = inst.archivable
        lifecycle.retrievable = inst.retrievable
        lifecycle.archiveStatusMessage = "datasetCreated"
        lifecycle.retrieveStatusMessage = inst.retrieveStatusMessage
        lifecycle.lastUpdateMessage = inst.lastUpdateMessage
        lifecycle.archiveReturnMessage = inst.archiveReturnMessage
        lifecycle.dateOfLastMessage = inst.dateOfLastMessage
        lifecycle.dateOfDiskPurging = inst.dateOfDiskPurging
        lifecycle.archiveRetentionTime = inst.archiveRetentionTime
        lifecycle.isExported = inst.isExported
        lifecycle.exportedTo = inst.exportedTo
        lifecycle.dateOfPublishing = inst.dateOfPublishing
        lifecycle.ownerGroup = inst.ownerGroup
        lifecycle.accessGroups = inst.accessGroups
        lifecycle.createdBy = inst.createdBy
        lifecycle.updatedBy = inst.updatedBy
        lifecycle.datasetId = str(my_data_set.pid)
        lifecycle.createdAt = current_date
        lifecycle.updatedAt = current_date
        return lifecycle

    def get_date_information(self, basename, directory_path):
        year_month = "2018_01"
        search_result = re.search(self.year_month_regex, directory_path)
        if search_result:
            year_month = search_result.group(0)
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


if __name__ == '__main__':
    start_time = time.time()
    g = GenerateMetadata()
    g.generate()
    print("--- %s seconds ---" % (time.time() - start_time))

