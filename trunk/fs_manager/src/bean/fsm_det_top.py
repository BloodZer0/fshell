# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web bean层_TOP事件


if __name__ == "__main__":
    import sys
    import os

    sys.path.append("../base")
    sys.path.append("..")
    sys.path.append("../dao")

from fsm_cfg import *
from fs_util import *


# from fsm_result_fileatt_dao import *


class FsmDetTop:

    @staticmethod
    def get_sum_list(userId, topCount):
        sumList = [
            {"file_id": 1009, "filename":"cmd-recv.php", "statics": 14.15, "fileatt": 81.11, "weblog": 25.5, "danfunc":63, "fuzzhash": 91, "synthetic": 0.912},
            {"file_id": 1002, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1003, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1005, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1007, "filename":"include-shell.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1012, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1032, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1022, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1045, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1089, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1090, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1062, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892}
        ]

        return sumList


    @staticmethod
    def get_weblog_list(userId, topCount):
        weblogList = [
            {"file_id": 1009, "filename":"cmd-recv.php", "statics": 14.15, "fileatt": 81.11, "weblog": 25.5, "danfunc":63, "fuzzhash": 91, "synthetic": 0.912},
            {"file_id": 1002, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1003, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1005, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1007, "filename":"include-shell.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1012, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1032, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1022, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1045, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1089, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1090, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892},
            {"file_id": 1062, "filename":"include-shell-recv.php", "statics": 12.45, "fileatt": 78.21, "weblog": 23.5, "danfunc":67, "fuzzhash": 95, "synthetic": 0.892}
        ]

        return weblogList

    
    @staticmethod
    def get_sum_list(userId, topCount):      


        return 0



    @staticmethod
    def det_top_list(userId, topCount):

        topList = {
            "top_sum": FsmDetTop.get_sum_list(userId, topCount),
            "top_weblog": FsmDetTop.get_weblog_list(userId, topCount),
            "top_sum3": FsmDetTop.get_sum_list(userId, topCount),
            "top_sum4": FsmDetTop.get_sum_list(userId, topCount)
        }

        return True, topList
