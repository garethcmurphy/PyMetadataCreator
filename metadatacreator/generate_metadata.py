#!/usr/bin/env python3
"""generate metadata"""
import datetime
import json
import re
import socket
import time

from sortedcontainers import SortedDict

from Base64Im import Base64Im
from files_info import FilesInfo
from instrumentfactory import InstrumentFactory
from sdk.swagger_client.models.dataset_lifecycle import DatasetLifecycle
from sdk.swagger_client.models.orig_datablock import OrigDatablock
from sdk.swagger_client.models.published_data import PublishedData
from sdk.swagger_client.models.raw_dataset import RawDataset


class GenerateMetadata:
    """generate metadata"""

    def __init__(self):
        self.global_file_number = 0
        self.met_directory = "./data/experiments"
        self.year_month_regex = '20[0-9]{2}_[0-1][0-9]'
        self.hostname = socket.gethostname()
        image = Base64Im()
        self.image = image.im

        self.location = 'local'
        self.handle_prefix = '20.500.12269'
        if self.hostname == 'login.esss.dk':
            self.location = 'remote'
        if self.hostname in ("macmurphy.local", "CI0020036"):
            self.location = 'local'

    def generate(self):
        """generate metadata"""

        data_sets = SortedDict()
        experiments = [
            'v20',
            'sonde',
            'nmx',
            'multiblade',
            'multigrid',
        ]

        for i in range(0, 5):
            # print(i)
            experiment = experiments[i]
            print(experiment)

            new_inst = InstrumentFactory()
            inst = new_inst.factory(experiment)

            data_set_num = 0
            for key, source_folder_fragment in inst.source_folder_array.items():
                source_folder = self.met_directory + '/' + source_folder_fragment
                if self.location is 'local':
                    source_folder = "demo"
                data_set_num = data_set_num + 1
                files_info = FilesInfo()
                files_info.extract_file_list(source_folder)
                self.global_file_number += files_info.file_number

                met_data_set = self.get_dataset(
                    key, inst, data_set_num, files_info)
                met_orig = self.get_orig_blocks(met_data_set, inst, files_info)
                met_published = self.get_published_data(
                    inst, met_data_set, files_info, key)
                met_lifecycle = self.get_lifecycle(inst, met_data_set)

                scicat_entries = {
                    "dataset": met_data_set.to_dict(),
                    "orig": met_orig.to_dict(),
                    "published": met_published.to_dict(),
                    "lifecycle": met_lifecycle.to_dict()
                }
                data_sets[
                    "orig" + files_info.experiment_date_time + str(i).zfill(5) + str(data_set_num).zfill(
                        5)] = scicat_entries
        print("Files processed =", self.global_file_number)
        with open('test_new_metadata.json', 'w') as f:
            json.dump(data_sets, f, ensure_ascii=False, indent=2)

    def get_dataset(self, key, inst, data_set_number, files_info):
        met_data_set = RawDataset()
        # print(inst.abbreviation)
        met_data_set.principalInvestigator = inst.principalInvestigator
        met_data_set.endTime = inst.endTime
        met_data_set.creationLocation = inst.creationLocation
        met_data_set.owner = inst.owner
        met_data_set.ownerEmail = inst.ownerEmail
        met_data_set.orcidOfOwner = inst.orcidOfOwner
        met_data_set.contactEmail = inst.contactEmail

        met_data_set.pid = self.handle_prefix + '/BRIGHTNESS/' + \
            inst.abbreviation + str(data_set_number).zfill(4)
        print(met_data_set.pid, end='\r')
        met_data_set.size = files_info.total_file_size
        met_data_set.packedSize = files_info.total_file_size
        met_data_set.creationTime = files_info.experiment_date_time
        met_data_set.endTime = files_info.experiment_date_time
        met_data_set.createdAt = files_info.experiment_date_time
        met_data_set.updatedAt = files_info.experiment_date_time
        met_data_set.doi = inst.doi + str(data_set_number).zfill(4)
        met_data_set.sourceFolder = files_info.source_folder
        # print(key)
        if key in inst.metadata_object:
            met_data_set.scientificMetadata = inst.metadata_object[key]
        else:
            met_data_set.scientificMetadata = inst.scientificMetadata
        met_data_set.proposalId = inst.proposal
        met_data_set.validationStatus = inst.validationStatus
        met_data_set.keywords = inst.keywords
        met_data_set.description = inst.dataDescription
        met_data_set.userTargetLocation = inst.userTargetLocation
        met_data_set.classification = inst.classification
        met_data_set.license = inst.license
        met_data_set.version = inst.version
        met_data_set.type = inst.type
        met_data_set.ownerGroup = inst.ownerGroup
        met_data_set.accessGroups = inst.accessGroups
        met_data_set.createdBy = inst.createdBy
        met_data_set.updatedBy = inst.updatedBy
        met_data_set.sampleId = inst.sampleId
        met_data_set.isPublished = inst.isPublished
        met_data_set.dataFormat = inst.resourceType

        return met_data_set

    @staticmethod
    def get_orig_blocks(met_data_set, inst, file_info):
        """get orig blocks"""
        met_orig = OrigDatablock()
        met_orig.datasetId = str(met_data_set.pid)
        met_orig.rawDatasetId = met_orig.datasetId
        met_orig.derivedDatasetId = met_orig.datasetId
        met_orig.dataFileList = file_info.file_list
        met_orig.size = file_info.total_file_size
        met_orig.createdAt = file_info.experiment_date_time
        met_orig.updatedAt = file_info.experiment_date_time
        met_orig.ownerGroup = inst.ownerGroup
        met_orig.accessGroups = inst.accessGroups
        met_orig.createdBy = inst.createdBy
        met_orig.updatedBy = inst.updatedBy
        return met_orig

    def get_published_data(self, inst, met_data_set, file_info, key):
        """get published data """
        met_published = PublishedData()
        met_published.doi = str(met_data_set.doi)
        met_published.affiliation = inst.affiliation
        met_published.publisher = inst.publisher
        met_published.creator = inst.creator
        met_published.title = inst.title
        met_published.publicationYear = inst.publicationYear
        met_published.publisher = inst.publisher
        met_published.resourceType = inst.resourceType
        met_published.abstract = inst.abstract
        met_published.thumbnail = self.image
        met_published.url = inst.url + key
        met_published.sizeOfArchive = file_info.total_file_size
        met_published.numberOfFiles = file_info.file_number
        met_published.dataDescription = inst.dataDescription
        met_published.authors = inst.authors
        met_published.pidArray = inst.pidArray
        met_published.doiRegisteredSuccessfullyTime = inst.doiRegisteredSuccessfullyTime
        return met_published

    @staticmethod
    def get_lifecycle(inst, met_data_set):
        """get dataset lifecycle """
        current_date = datetime.datetime.now().isoformat()
        lifecycle = DatasetLifecycle()
        lifecycle.id = str(met_data_set.pid)
        lifecycle.isOnDisk = inst.isOnDisk
        lifecycle.isOnTape = inst.isOnTape
        lifecycle.isOnCentralDisk = inst.isOnTape
        lifecycle.archivable = inst.archivable
        lifecycle.retrievable = inst.retrievable
        lifecycle.archiveStatusMessage = "datasetCreated"
        lifecycle.retrieveStatusMessage = inst.retrieveStatusMessage
        lifecycle.lastUpdateMessage = inst.lastUpdateMessage
        lifecycle.archiveReturnMessage = inst.archiveReturnMessage
        lifecycle.MessageHistory = inst.MessageHistory
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
        lifecycle.datasetId = str(met_data_set.pid)
        lifecycle.rawDatasetId = lifecycle.datasetId
        lifecycle.derivedDatasetId = lifecycle.datasetId
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
        data_date = datetime.datetime(int(year), int(month), int(day))
        experiment_date_time = data_date.isoformat()
        return experiment_date_time


if __name__ == '__main__':
    START_TIME = time.time()
    GEN = GenerateMetadata()
    GEN.generate()
    print("--- %s seconds ---" % (time.time() - START_TIME))
