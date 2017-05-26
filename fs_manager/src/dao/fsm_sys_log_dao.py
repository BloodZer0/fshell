# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-15
# desc: dao sys_log表操作

'''
# sys_log表
CREATE TABLE `tb_sys_log` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `user_id` int(11) NOT NULL,
    `log_content` varchar(255) NOT NULL,
    `log_attr` text,
    `log_result` varchar(32) NOT NULL,
    `log_reason` varchar(255) DEFAULT NULL,
    `referee` varchar(255) NOT NULL,
    `remote_addr` varchar(32) NOT NULL,
    `insert_tm` datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''


from fs_util import *
from fs_database_pid import *
from fs_time import *


class FsmSysLogDao:

    @staticmethod
    def insert_node(userId, userName, remoteAddr, content, logAttr, logResult, logReason):
        dataBase = DataBase()
        sql = "insert into tb_sys_log(user_id, log_content, log_attr, log_result, log_reason, " \
              "referee, remote_addr, insert_tm) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        param = (userId, content, logAttr, logResult, logReason, userName, remoteAddr, get_cur_time())

        bRet, sRet = dataBase.insert_data(sql, param)
        return bRet, sRet



