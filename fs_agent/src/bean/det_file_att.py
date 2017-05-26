# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-13
# desc: detection file attribute


import sys
import os
import re

if __name__ == "__main__":
    sys.path.append("../base")

from fs_log import *
from fs_util import *
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


class FsaTaskFileatt:
    
    def __init__(self):
        self.web_dir = BaseConf.WEB_DIR
        self.out_file = BaseConf.CACHE_DIR + "/" + BaseConf.FILEATT_RESULT
        self.out_file_tmp = self.out_file + ".tmp"
        scan_file_ext = BaseConf.FILEATT_SCAN_FILE_EXT
        ext_regex = scan_file_ext.replace(".", "\.")
        self.regex = re.compile("(%s)$" % (ext_regex))

        tests = []
        tests.append(FileCtime())
        tests.append(FileMtime())
        tests.append(FilePriv())
        tests.append(FileOwner())
        self.tests = tests

        self.locator = SearchFile_V2()
        self.cachedb = GetCacheDb()


    def start_task(self):
        bRet, rows_db_tmp, fileList = self.cachedb.write_cache_db_tmp(self.out_file_tmp, self.tests, self.locator, self.web_dir, self.regex)
        if not bRet:
            return False, 'calc or write result ERR'

        bRet, rows_db = self.cachedb.read_cache_db(self.out_file)
        if not bRet:
            os.rename(self.out_file_tmp, self.out_file)
        else:
            bRet, rows_db_tmp = self.cachedb.get_changed_data(rows_db_tmp, fileList, rows_db)
            if not bRet: rows_db_tmp = None
            os.rename(self.out_file_tmp, self.out_file)

        bRet, sRet = FsaTaskClient.report_task(FsaTaskType.F_FILEATT, FsaTaskStatus.T_FINISH, rows_db_tmp)
        if not bRet:
            Log.err("Report task file attribute ERR: %s" % (sRet))


