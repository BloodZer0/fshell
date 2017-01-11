# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-08
# desc: data_weblog


import sys
sys.path.append("../dao")
from fss_data_weblog_dao import *


class FssWebLog:
    
    @staticmethod
    def insert_node(agent_id, data):
        
        time_local = data['time_local']
        data['time_local'] = time_local[1:20]


        return FssWebLogDao.insert_node(agent_id, data)


