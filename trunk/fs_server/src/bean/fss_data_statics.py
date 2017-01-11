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
        data['text_lw'] = int(data['text_lw'])

        return FssStaticsDao.insert_node(agent_id, data)


