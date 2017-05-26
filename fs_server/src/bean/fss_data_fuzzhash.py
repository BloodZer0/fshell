# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-08
# desc: data_fuzzhash


import sys
sys.path.append("./dao")
from fss_data_fuzzhash_dao import *


class FssFuzzHash:
    
    @staticmethod
    def insert_node(agent_id, data):
        if not isinstance(data, list):
            return False, "valid reqJson of data"

        if len(data) == 0:
            return True, ""

        for item in data:
            if item.has_key('deleted'):
                continue

            dataCnt = {
                "filename": item['filename'],
                "fuzz_hash": item['FuzzHash']
            }
            bRet, sRet = FssFuzzHashDao.insert_node(int(agent_id), dataCnt)
            if not bRet:
                Log.err("insert fuzz_hash err: %s" % (str(sRet)))

        return True, "" #FssFuzzHashDao.insert_node(int(agent_id), dataCnt)
