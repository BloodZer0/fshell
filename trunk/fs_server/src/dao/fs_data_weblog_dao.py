# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-06
# desc: data_weblog

'''
# web日志-元数据表
CREATE TABLE `tb_data_weblog` (
    `id` varchar(20) NOT NULL,
    `agent_id` int(11) NOT NULL,
    `client_ip` varchar(20) NOT NULL,
    `time_local` datetime NOT NULL,
    `method` varchar(6) NOT NULL,
    `url` varchar(200) NOT NULL,
    `req_body` text NOT NULL,
    `referer` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''


import sys
sys.path.append("..")
sys.path.append("../base")

from fss_cfg import *
from fs_util import *
from fs_database_pid import *


class FsWebLogDao:
    
    @staticmethod
    def  insert_node(agent_id, data):
        client_ip = data['client_ip']
        time_local = data['time_local']
        method = data['method']
        url = data['url']
        req_body = data['req_body']
        referer = data['referer']


        dataBase = DataBase()
        sql = "insert into tb_data_weblog(agent_id, client_ip, time_local, method, url, \
              req_body, referer) values(%s, %s, %s, %s, %s, %s, %s)";
        param = (agent_id, client_ip, time_local, method, url, req_body, referer)
        
        bRet, sRet = DataBase.insert_data(sql, param)
        if not bRet:
            return False, sRet

        return True, sRet



