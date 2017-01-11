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

        return FssDanFuncDao.insert_node(agent_id, data)
