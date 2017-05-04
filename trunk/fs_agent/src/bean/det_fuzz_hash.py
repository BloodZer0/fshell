# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-13
# desc: detection file fuzzy hash


import sys
import os
import re
import pyssdeep

if __name__ == "__main__":
    sys.path.append("../base")


from fs_log import *
from fs_util import *
from fs_base_cfg import *
from fsa_task import *
from fsa_task_type import *


class FuzzHash:

    def calculate(self, filename):
        return pyssdeep.fuzzy_hash_filename(filename)


class FsaTaskFuzzhash:
    
    def __init__(self):
        self.web_dir = BaseConf.WEB_DIR
        self.out_file = BaseConf.CACHE_DIR + "/" + BaseConf.FUZZHASH_RESULT
        self.out_file_tmp = self.out_file + ".tmp"
        scan_file_ext = BaseConf.FUZZHASH_SCAN_FILE_EXT
        ext_regex = scan_file_ext.replace(".", "\.")
        self.regex = re.compile("(%s)$" % (ext_regex))

        self.tests = [FuzzHash()]
        self.locator = SearchFile_V2()
        self.cachedb = GetCacheDb()
        

    def start_task(self):
        F_Flag = True

        bRet, rows_db_tmp, fileList = self.cachedb.write_cache_db_tmp(self.out_file_tmp, self.tests, self.locator, self.web_dir, self.regex)
        if not bRet:
            return False, 'calc or write result ERR'

        bRet, rows_db = self.cachedb.read_cache_db(self.out_file)
        if not bRet:
            os.unlink(self.out_file)
            os.rename(self.out_file_tmp, self.out_file)
            F_Flag = False

        # find the no need source file from the
        # rows_db and append it to the rows_db_tmp list.
        if F_Flag:
            for item in rows_db:
                if item['filename'] in fileList:
                    continue

                item = {"filename": item["filename"], "deleted": 1}
            rows_db_tmp.append(item)

        bRet, sRet = FsaTaskClient.report_task(FsaTaskType.F_FUZZHASH, FsaTaskStatics.T_FINISH, rows_db_tmp)
        if not bRet:
            Log.err("Report fuzzy hash ERR: %s" % (sRet))
            #
            # bababa...


