# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-06
# desc: data_danfunc

'''
# 危险函数-元数据表
CREATE TABLE `tb_data_danfunc` (
    `id` varchar(20) NOT NULL,
    `agent_id` int(11) NOT NULL,
    `filename` varchar(50) NOT NULL,
    `weight_sum` int(5) NOT NULL,
    `functions` text NOT NULL,
    `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

import sys
sys.path.append("..")
sys.path.append("../base")

from fs_cfg import *
from fs_util import *
from fs_database_pid import *




class FsDanFuncDao:
    
    @staticmethod
    def insert_node(agent_id, data):
        filename = data['filename']
        weight_sum = data['weight_sum']
        functions = data['functions']

        dataBase = DataBase()
        sql = "insert into tb_data_danfunc(agent_id, filename, weight_sum, functions, insert_tm) values(%s, %s, %s, %s, %s)"
        param = (agent_id, filename, weight_sum, functions, get_cur_time())

        bRet, sRet = dataBase.insert_data(sql, param)
        if not bRet:
            return False, sRet

        return True, sRet




