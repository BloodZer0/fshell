# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-08
# desc: data_fileatt


import sys
sys.path.append("../dao")
from fss_data_fileatt_dao import *


class FssFileAtt:
    
    @staticmethod
    def insert_node(agent_id, data):
        if not isinstance(data, list):
            return False, "valid reqJson of data"

        if len(data)==0:
            return True, ""

        for item in data:
            if item.has_key('deleted'):
                continue

            dataCnt = {
                "filename": item['filename'],
                "file_ctime": item['FileCtime'],
                "file_mtime": item['FileMtime'],
                "file_mode": item['FilePriv'],
                "file_owner": item['FileOwner']
            }
            bRet, sRet = FssFileAttDao.insert_node(int(agent_id), dataCnt)
            if not bRet:
                Log.err("insert file_att err: %s" % (str(sRet)))

        return True, "" #FssFileAttDao.insert_node(int(agent_id), dataCnt)


