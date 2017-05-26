# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-06
# desc: data_fuzzhash 

'''
# fuzz_hash-元数据表
CREATE TABLE `tb_data_fuzzhash` (
    `id` varchar(20) NOT NULL,
    `agent_id` int(11) NOT NULL,
    `filename` varchar(200) NOT NULL,
    `fuzz_hash` varchar(300) NOT NULL,
    `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''


import sys
sys.path.append("..")
sys.path.append("../base")

from fss_cfg import *
from fss_util import *
from fss_database_pid import *


class FssFuzzHashDao:
    
    @staticmethod
    def insert_node(agent_id, data):
        filename = data['filename']
        fuzz_hash = data['fuzz_hash']
        
        dataBase = DataBase()
        sql = "insert into tb_data_fuzzhash(agent_id, filename, fuzz_hash, insert_tm) values(%s, %s, %s, %s)"
        param = (agent_id, filename, fuzz_hash, get_cur_time())

        bRet, sRet = dataBase.insert_data(sql, param)
        if not bRet:
            return False, sRet

        return True, sRet

