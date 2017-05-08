# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-13
# desc: detection statistics 
# the kernel algorithm are learning
# from neopi.py and thanks for @Neohapsis.


import sys
import os
import re
import zlib
import math
from collections import defaultdict

if __name__ == "__main__":
    sys.path.append("../base")

from fs_log import *
from fs_util import *
from fs_base_cfg import *
from fsa_task import *
from fsa_task_type import *


class LanguageIC:
    def __init__(self):
        self.char_count = defaultdict(int)
        self.total_char_count = 0
        self.results = []
        self.ic_total_results = ""

    def calculate(self, filename):
        data = open(filename, 'rb').read()

        if not data: return 0
        char_count = 0
        total_char_count = 0

        for x in range(256):
            char = chr(x)
            charcount = data.count(char)
            char_count += charcount * (charcount - 1)
            total_char_count += charcount

        ic = float(char_count)/(total_char_count * (total_char_count - 1))
        return ("%.8f" % ic)


class Entropy:
    def __init__(self):
        self.results = []

    def calculate(self, filename):
        data = open(filename, 'rb').read()

        if not data: return 0
        entropy = 0
        self.stripped_data = data.replace(' ', '')
        for x in range(256):
            p_x = float(self.stripped_data.count(chr(x)))/len(self.stripped_data)
            if p_x > 0:
                entropy += - p_x * math.log(p_x, 2)
        return ("%.8f" % entropy)


class LongestWord:
    def __init__(self):
        self.results = []

    def calculate(self, filename):
        data = open(filename, 'rb').read()

        if not data:
            return "", 0
        longest = 0
        longest_word = ""
        words = re.split("[\s,\n,\r]", data)
        if words:
            for word in words:
                length = len(word)
                if length > longest:
                    longest = length
                    longest_word = word
        return longest


class Compression:
    def __init__(self):
        self.results = []

    def calculate(self, filename):
        data = open(filename, 'rb').read()

        if not data:
            return "", 0
        compressed = zlib.compress(data)
        ratio = float(len(compressed)) / float(len(data))
        return ("%.8f" % ratio)


class FsaTaskStatics:
    
    def __init__(self):
        self.web_dir = BaseConf.WEB_DIR
        self.out_file = BaseConf.CACHE_DIR + "/" + BaseConf.STATICS_RESULT
        self.out_file_tmp = self.out_file + ".tmp"
        scan_file_ext = BaseConf.STATICS_SCAN_FILE_EXT
        ext_regex = scan_file_ext.replace(".", "\.")
        self.regex = re.compile("(%s)$" % (ext_regex))

        tests = []
        tests.append(LanguageIC())
        tests.append(Entropy())
        tests.append(LongestWord())
        tests.append(Compression())
        self.tests = tests

        self.locator = SearchFile()
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

        bRet, sRet = FsaTaskClient.report_task(FsaTaskType.F_STATICS, FsaTaskStatus.T_FINISH, rows_db_tmp)
        if not bRet:
            Log.err("Report statistics ERR: %s" % (sRet))





