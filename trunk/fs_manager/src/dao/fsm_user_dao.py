# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-15
# desc: dao user表操作

'''
# 用户表
CREATE TABLE `tb_user_pwd` (
    `user_id` int(11) NOT NULL,
    `username` varchar(30) NOT NULL,
    `password` varchar(30) NOT NULL,
    `email` varchar(30) NOT NULL,
    `phone` varchar(20) DEFAULT NULL,
    `priv` int(2) NOT NULL DEFAULT '1',
    `remark` varchar(50) DEFAULT NULL,
    `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

if __name__ == "__main__":
    import sys
    
    sys.path.append("..")
    sys.path.append("../base")
    from fsm_cfg import *

from fs_util import *
from fs_time import *
from fs_database_pid import *


class FsmUserDao:

    @staticmethod
    def insert_node(username, password, email, phone, priv, remark):
        dataBase = DataBase()
        sql = "insert into tb_user_pwd(username, password, email, phone, priv, remark, insert_tm) " \
              "values(%s, %s, %s, %s, %s, %s, %s)"
        param = (username, password, email, phone, priv, remark, get_cur_time())

        bRet, sRet = dataBase.insert_data(sql, param)

        return bRet, sRet

    @staticmethod
    def query_node_u(userId):

        dataBase = DataBase()
        sql = "select * from tb_user_pwd where user_id = %s"
        param = (userId,)

        bRet, sRet = dataBase.query_data(sql, param)
        if not bRet:  return False, sRet

        if sRet is None or len(sRet) <= 0:
            return False, "userId (%s) not exist" % (userId)
        return bRet, sRet[0]


    @staticmethod
    def query_node_un(userName):
        dataBase = DataBase()
        sql = "select * from tb_user_pwd where username = %s"
        param = (userName,)

        bRet, sRet = dataBase.query_data(sql, param)

        if not bRet:  return False, sRet

        if sRet == None or len(sRet) <= 0:
            return False, "user(%s) not exist record" % (userName)

        return bRet, sRet[0]


    @staticmethod
    def query_nodes():
        dataBase = DataBase()
        sql = "select * from tb_user_pwd"
        bRet, sRet = dataBase.query_data(sql, None)
        if not bRet: return bRet, sRet

        if len(sRet) <= 0: return False, "no record exist."

        return bRet, sRet
