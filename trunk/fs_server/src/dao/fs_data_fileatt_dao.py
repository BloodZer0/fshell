# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-06
# desc: data_fileatt

'''
# 文件属性-元数据表
CREATE TABLE `tb_data_fileatt` (
    `id` varchar(20) NOT NULL,
    `agent_id` int(11) NOT NULL,
    `filename` varchar(50) NOT NULL,
    `file_ctime` datetime NOT NULL,
    `file_mtime` datetime NOT NULL,
    `file_mode` int(5) NOT NULL,
    `file_owner` varchar(20) NOT NULL,
    `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''


if __name__ == "__main__":
    import sys
    sys.path.append("..")
    sys.path.append("../base")

from fs_cfg import *
from fs_util import *
from fs_database_pid import *


class FsFileAttDao:
    
    @staticmethod
    def insert_node(agent_id, data):
        filename = data['filename']
        file_ctime = data['file_ctime']
        file_mtime = data['file_mtime']
        file_mode = data['file_mode']
        file_owner = data['file_owner']

        dataBase = DataBase()
        sql = "insert into tb_data_fileatt(agent_id, filename, file_ctime, file_mtime, file_mode, \
              file_owner, insert_tm) values(%s, %s, %s, %s, %s, %s, %s)"
        param = (agent_id, filename, file_ctime, file_mtime, file_mode, file_owner, get_cur_time())

        bRet, sRet = dataBase.insert_data(sql, param)
        if not bRet:
            return False, sRet

        return True, sRet


