# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-13
# desc: detection file attribute


import sys
import os
import re
import csv

if __name__ == "__main__":
    sys.path.append("../base")

from fs_log import *
from fs_base_cfg import *
from fsa_task import *
from fsa_task_type import *


class FileCtime:
    def calculate(self, filename):
        return int(os.path.getctime(filename))


class FileMtime:
    def calculate(self, filename):
        return int(os.path.getmtime(filename))

class FilePriv:
    def calculate(self, filename):
        return oct(os.stat(filename).st_mode)[-3:]

class FileOwner:
    def calculate(self, filename):
        return [os.stat(filename).st_uid, os.stat(filename).st_gid]


class SearchFile:

    def search_file_path(self, web_dir, regex):
        for root, dirs, files in os.walk(web_dir):
            for file in files:
                filename = os.path.join(root, file)

                if not re.search(regex, filename):
                    continue

                filesize = os.path.getsize(filename)
                
                yield filesize, filename



class FsaTaskFileatt:
    
    def __init__(self):
        self.web_dir = BaseConf.WEB_DIR
        self.out_file = BaseConf.CACHE_DIR + "/" + BaseConf.FILEATT_RESULT
        self.out_file_tmp = self.out_file + ".tmp"
        scan_file_ext = BaseConf.FILE_SCAN_FILE_EXT
        ext_regex = scan_file_ext.replace(".", "\.")
        self.regex = re.compile("(%s)$" % (ext_regex))
        self.fileList = []

        tests = []
        tests.append(FileCtime())
        tests.append(FileMtime())
        tests.append(FilePriv())
        tests.append(FileOwner())
        self.tests = tests

        self.locator = SearchFile()


    def _read_local_db(self):
        
        if not os.path.exists(self.out_file):
            return False, None
        
        with open(self.out_file) as f:
            f_csv = csv.DictReader(f)
        
        return True, f_csv


    def _write_local_db_tmp(self):
        
        csv_rows = list()
        csv_headers = ["filename"]

        for filesize, filename in self.locator.search_file_path(web_dir, regex):
            if filesize == 0: continue

            calc_value = dict()
            for test in tests:
                test_name = test.__class__.__name__
                calc_value[test_name] = test.calculate(filename)
                if len(csv_headers) < len(test) +1:
                    csv_headers.append(test_name)
            
            csv_rows.append(calc_value)
            self.fileList.append(filename)
            
        with open(self.out_file_tmp) as f:
            f_csv = csv.DictWriter(f, csv_headers)
            f_csv.writeheader()
            f_csv.writerows(csv_rows)
        
        return True, csv_rows


    def start_task(self):
        F_Flag = True

        bRet, rows_db_tmp = self._write_local_db_tmp()
        if not bRet:
            return False, 'calc or write result ERR'

        bRet, rows_db = self._read_local_db()
        if not bRet:
            os.unlink(self.out_file)
            os.rename(self.out_file_tmp, self.out_file)
            F_Flag = False

        # find the no need source file from the
        # rows_db and append it to the rows_db_tmp list.
        if F_Flag:
            for item in rows_db:
                if item['filename'] in self.fileList:
                    continue

                item = {"filename": item["filename"], "deleted": 1}
            rows_db_tmp.append(item)

        bRet, sRet = FsaTaskClient.report_task(FsaTaskType.F_STATICS, FsaTaskStatics.T_FINISH, rows_db_tmp)
        if not bRet:
            Log.err("Report statistics ERR: %s" % (sRet))
            #
            # bababa...


