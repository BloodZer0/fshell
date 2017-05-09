# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-08
# desc: data_danfunc 



import sys
sys.path.append("../dao")
from fss_data_danfunc_dao import *


class FssDanFunc:
    
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
                "weight_sum": 0,
                "functions": str(','.join(item['funclist']))
            }
            bRet, sRet = FssDanFuncDao.insert_node(int(agent_id), dataCnt)
            if not bRet:
                Log.err("insert dan_func err: %s" % (str(sRet)))

        return True, "" #FssDanFuncDao.insert_node(int(agent_id), dataCnt)