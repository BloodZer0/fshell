# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-21
# desc: detection danger func


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


class Md5Hash:

    def calculate(self, filename):
        return compute_md5_file(filename)


class FsaTaskDanfunc:

    def __init__(self):
        self.web_dir = BaseConf.WEB_DIR
        self.out_file = BaseConf.CACHE_DIR + "/" + BaseConf.DANFUNC_RESULT
        self.out_file_tmp = self.out_file + ".tmp"
        scan_file_ext = BaseConf.DANFUNC_SCAN_FILE_EXT
        ext_regex = scan_file_ext.replace(".", "\.")
        self.regex = re.compile("(%s)$" % (ext_regex))

        self.tests = [Md5Hash()]
        self.locator = SearchFile()
        self.cachedb = GetCacheDb()


    def _get_all_funcs(self, filename):
        regex = re.compile(r"""([a-zA-Z|@]\w+)\(["\w+"|"\w+",|'\w+'|'\w+',|\$\w+|\$\w+,]*\)""")
        try:
            content = open(filename, "rb").read()
        except:
            return False, None

        result = re.findall(regex, content)

        return True, result


    def start_task(self):
        F_Flag = True

        bRet, rows_db_tmp, fileList = self.cachedb.write_cache_db_tmp(self.out_file_tmp, self.tests, self.locator, self.web_dir,, self.regex)
        if not bRet:
            return False, 'calc or write result ERR'

        bRet, rows_db = self.cachedb.read_cache_db(self.out_file)
        if not bRet:
            os.unlink(self.out_file)
            os.rename(self.out_file_tmp, self.out_file)
            F_Flag = False

        # find the no need source file from the
        # rows_db and append it to the rows_db_tmp list.
        dataList = list()
        if F_Flag:
            for item in rows_db:
                filename = item["filename"]
                if filename in fileList: continue
                
                item = {"filename": filename, "deleted": 1}
                dataList.append(item)

        # get the db_tmp's file funcs.
        for filename in fileList:
            bRet, funcList = self._get_all_funcs(filename)
            if not bRet:
                Log.err("Could not read: %s" % (filename))
                item = {"filename": filename, "bad_read": 1}
            else:
                item = {"filename":filename, "funclist": funcList}

            dataList.append(item)


        bRet, sRet = FsaTaskClient.report_task(FsaTaskType.F_FUZZHASH, FsaTaskStatics.T_FINISH, dataList)
        if not bRet:
            Log.err("Report fuzzy hash ERR: %s" % (sRet))
            #
            # bababa...







