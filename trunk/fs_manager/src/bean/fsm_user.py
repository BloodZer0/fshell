# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web bean层_User管理


if __name__ == "__main__":
    import sys
    import os

    sys.path.append("../base")
    sys.path.append("..")
    sys.path.append("../dao")

from fsm_cfg import *
from fs_util import *
from fsm_user_dao import *


class FsmUser:

    @staticmethod
    def login(userName, password):
        bRet, record = fsmUserDao.query_node_un(userName)
        if not bRet:  return False, u"用户名或密码错误"

        if record['password'] != comput_md5_text('fshell#' + password):
            return False, u'用户名或密码错误'

        userInfo = {
            "user_id": record['user_id'],
            "userame": record['username'],
            "email": record['email'],
            "priv": record['priv']
        }

        return True, userInfo

    @staticmethod
    def get_user_id(userName):
        bRet, record = fsmUserDao.query_node_un(userName)
        if not bRet:
            return False, record

        return True, record['user_id'] 


    @staticmethod
    def get_user_list(userId):
        pass

