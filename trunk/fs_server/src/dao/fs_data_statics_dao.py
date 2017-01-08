# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-06
# desc: data_statics
'''
# 统计学-元数据表
CREATE TABLE `tb_data_statics` (
    `id` varchar(20) NOT NULL,
    `agent_id` int(11) NOT NULL,
    `filename` varchar(50) NOT NULL,
    `text_ic` varchar(10) NOT NULL,
    `text_ent` varchar(10) NOT NULL,
    `text_lw` int(11) NOT NULL,
    `text_cmp` varchar(10) NOT NULL,
    `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''


import sys
sys.path.append("..")
sys.path.append("../base")

from fss_cfg import *
from fs_util import *
from fs_database_pid import *


class FsStaticsDao:
    
    @staticmethod
    def inert_node(agent_id, data):
        filename = data['filename']
        text_ic = data['text_ic']
        text_ent = data['text_ent']
        text_lw = data['text_lw']
        text_cmp = text_cmp['text_cmp']

        dataBase = DataBase()
        sql = "insert into tb_data_statics(agent_id, filename, text_ic, text_ent, text_lw, \
                text_cmp, insert_tm) values(%s, %s, %s, %s, %s, %s %s)"
        param = (agent_id, filename, text_ic, text_ent, text_lw, text_lw, text_cmp, get_cur_time())

        bRet, sRet = dataBase.insert_data(sql, param)
        if not bRet:
            return False, sRet

        return True, sRet



