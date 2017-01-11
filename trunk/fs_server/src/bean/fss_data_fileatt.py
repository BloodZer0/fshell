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

        return FssFileAttDao.insert_node(agent_id, data)

