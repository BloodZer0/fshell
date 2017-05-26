# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web bean层_高危函数特征库


if __name__ == "__main__":
    import sys
    import os

    sys.path.append("../base")
    sys.path.append("..")
    sys.path.append("../dao")

from fsm_cfg import *
from fs_util import *



class FsmLibDanfunc:

    @staticmethod
    def lib_danfunc_list(userId, page, count):
        danfuncList = [
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-17"},
            {"id":1004, "func_name": "mysql_connect", "web_type":"php", "risk": 3, "remark":"connect mysql", "insert_tm":"2017-05-17"},
            {"id":1004, "func_name": "phpinfo", "web_type":"php", "risk": 4, "remark":"show php configure", "insert_tm":"2017-05-17"},
            {"id":1004, "func_name": "exec", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-16"},
            {"id":1004, "func_name": "system", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-16"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"},
            {"id":1004, "func_name": "eval", "web_type":"php", "risk": 7, "remark":"exec sys functions", "insert_tm":"2017-05-15"}
        ]

        return True, danfuncList