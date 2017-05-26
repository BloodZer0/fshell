# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-08
# desc: data_statics

import sys
sys.path.append("../dao")
from fss_data_statics_dao import *

class FssStatics:
   
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
                "text_ic": item['LanguageIC'],
                "text_ent": item['Entropy'],
                "text_lw": item['LongestWord'],
                "text_cmp": item['Compression']
            }
            bRet, sRet = FssStaticsDao.insert_node(int(agent_id), dataCnt)
            if not bRet:
                Log.err("insert statics err: %s" % (str(sRet)))

        return True, "" #FssStaticsDao.insert_node(agent_id, data)
