# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-08
# desc: data_weblog


import sys
sys.path.append("../dao")
from fss_data_weblog_dao import *


class FssWebLog:

    @staticmethod
    def format_time_str(time_local ,format='%Y-%m-%d %H:%M:%S'):
        try:
            time_local = time_local[1:20]
            struct_tm = time.strptime(time_local, '%d/%b/%Y:%H:%M:%S')
            return time.strftime(format, struct_tm)
        except:
            return ""

    
    @staticmethod
    def insert_node(agent_id, data):
        if not isinstance(data, list):
            return False, "valid reqJson of data"

        if len(data)==0:
            return True, ""

        for item in data:

            if not item.has_key('client_ip'):
                Log.err('ERR web log format: %s' % (str(item)))
                continue
            if not item.has_key('time_local'):
                Log.err('ERR web log format: %s' % (str(item)))
                continue
            if not item.has_key('status'):
                Log.err('ERR web log format: %s' % (str(item)))
                continue
            if not item.has_key('method'):
                Log.err('ERR web log format: %s' % (str(item)))
                continue
            if not item.has_key('url'):
                Log.err('ERR web log format: %s' % (str(item)))
                continue
            if not item.has_key('req_body'):
                Log.err('ERR web log format: %s' % (str(item)))
                continue
            if not item.has_key('referer'):
                Log.err('ERR web log format: %s' % (str(item)))
                continue

            dataCnt = {
                "client_ip": item['client_ip'],
                "time_local": FssWebLog.format_time_str(item['time_local']),
                "status": item['status'],
                "method": item['method'],
                "url": item['url'],
                "req_body": item['req_body'],
                "referer": item['referer']
            }

            print '>>>>>>', item['method']
            bRet, sRet = FssWebLogDao.insert_node(int(agent_id), dataCnt)
            if not bRet:
                Log.err("insert statics err: %s" % (str(sRet)))


        return True, "" #FssWebLogDao.insert_node(int(agent_id), dataCnt)


