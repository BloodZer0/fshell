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



class UserRole:
    SUPER_USER = 2
    BASE_USER =1


class FsmUser:

    @staticmethod
    def login(userName, password):
        bRet, record = FsmUserDao.query_node_un(userName)
        if not bRet:  return False, u"用户名或密码错误"

        if record['password'] != comput_md5_text('fshell#' + password):
            return False, u'用户名或密码错误'

        userInfo = {
            "user_id": record['user_id'],
            "username": record['username'],
            "email": record['email'],
            "user_role": record['role']
        }

        return True, userInfo

    @staticmethod
    def get_user_id(userName):
        bRet, record = FsmUserDao.query_node_un(userName)
        if not bRet:
            return False, record

        return True, record['user_id']

    @staticmethod
    def get_user_info(userId):
        bRet, record = FsmUserDao.query_node_u(userId)
        if not bRet:
            return False, record

        return True, record 

    @staticmethod
    def get_user_role(userId):
        bRet, record = FsmUserDao.query_node_u(userId)
        if not bRet:
            return False, record

        return True, record['role'] 
        

    @staticmethod
    def get_user_list(userId, userRole):
        if userRole == UserRole.SUPER_USER:
            bRet, sRet = FsmUserDao.query_nodes()
            if not bRet:
                return False, sRet

            userList = list()
            for item in sRet:
                userInfo = dict()
                userInfo['user_id'] = item['user_id']
                userInfo['user_name'] = item['username']
                userInfo['email'] = item['email']
                userInfo['phone'] = item['phone']
                userInfo['insert_tm'] = safe_datetime_to_str(item['insert_tm'])
                userInfo['role'] = int(item['role'])
                userList.append(userInfo)
            return True, userList
        else:
            bRet, userInfo = FsmUser.get_user_info(userId)
            if not bRet: return False, userInfo
            return True, [{
                'user_id': userInfo['user_id'],
                'user_name': userInfo['username'],
                'phone': userInfo['phone'],
                'email': userInfo['email'],
                'create_tm': safe_datetime_to_str(userInfo['insert_tm']),
                'role': userInfo['role'],
            }]

