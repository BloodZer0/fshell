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
import csv
import zlib
import math
from collections import defaultdict

if __name__ == "__main__":
    sys.path.append("../base")

from fs_log import *
from fs_base_cfg import *
from fsa_task import *
from fsa_task_type import *


class LanguageIC:
    def __init__(self):
        self.char_count = defaultdict(int)
        self.total_char_count = 0
        self.results = []
        self.ic_total_results = ""

    def calculate(self, data, filename):
        if not data: return 0
        char_count = 0
        total_char_count = 0

        for x in range(256):
            char = chr(x)
            charcount = data.count(char)
            char_count += charcount * (charcount - 1)
            total_char_count += charcount

        ic = float(char_count)/(total_char_count * (total_char_count - 1))
        return ic


class Entropy:
    def __init__(self):
        self.results = []

    def calculate(self, data, filename):
        if not data: return 0
        entropy = 0
        self.stripped_data = data.replace(' ', '')
        for x in range(256):
            p_x = float(self.stripped_data.count(chr(x)))/len(self.stripped_data)
            if p_x > 0:
                entropy += - p_x * math.log(p_x, 2)
        return entropy


class LongestWord:
    def __init__(self):
        self.results = []

    def calculate(self, data, filename):
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

    def calculate(self, data, filename):
        if not data:
            return "", 0
        compressed = zlib.compress(data)
        ratio = float(len(compressed)) / float(len(data))
        return ratio



class SearchFile:

    def __init__(self):
        self.smallest = BaseConf.SMALLEST_FILESIZE

    def search_file_path(self, web_dir, regex):
        for root, dirs, files in os.walk(web_dir):
            for file in files:
                filename = os.path.join(root, file)

                if not re.search(regex, filename):
                    continue

                if os.path.getsize(filename) < self.smallest:
                    continue
                
                try:
                    data = open(root + "/" + file, 'rb').read()
                except:
                    data = False
                    Log.err("Could not read file : %s/%s" % (root, file))
                yield data, filename




class FsaTaskStatics:
    
    def __init__(self):
        self.web_dir = BaseConf.WEB_DIR
        self.out_file = BaseConf.CACHE_DIR + "/" + BaseConf.STATICS_RESULT
        self.out_file_tmp = self.out_file + ".tmp"
        scan_file_ext = BaseConf.STATICS_SCAN_FILE_EXT
        ext_regex = scan_file_ext.replace(".", "\.")
        self.regex = re.compile("(%s)$" % (ext_regex))
        self.fileList = []

        tests = []
        tests.append(LanguageIC())
        tests.append(Entropy())
        tests.append(LongestWord())
        tests.append(Compression())
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

        for data, filename in self.locator.search_file_path(web_dir, regex):
            if not data: continue

            calc_value = dict()
            for test in tests:
                test_name = test.__class__.__name__
                calc_value[test_name] = test.calculate(data, filename)
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


