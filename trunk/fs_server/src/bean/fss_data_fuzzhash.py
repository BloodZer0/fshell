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

        return FssFuzzHashDao.insert_node(agent_id, data)
