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
    def get_sum_list(userId, sumCount):
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
    def get_weblog_list(userId, weblogCount):
        weblogList = [
            {"file_id": 1009, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 1, "keys":67.5, "pages": 32},
            {"file_id": 1010, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 0, "keys":63.5, "pages": 32},
            {"file_id": 1029, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 0, "keys":63.5, "pages": 32},
            {"file_id": 1006, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 0, "keys":63.5, "pages": 32},
            {"file_id": 1021, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 0, "keys":63.5, "pages": 32},
            {"file_id": 1049, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 0, "keys":61.5, "pages": 32},
            {"file_id": 1059, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 1, "keys":63.5, "pages": 32},
            {"file_id": 1067, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 0, "keys":63.5, "pages": 32},
            {"file_id": 1021, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 1, "keys":36.5, "pages": 32},
            {"file_id": 1009, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 0, "keys":63.4, "pages": 32},
            {"file_id": 1093, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 1, "keys":63.5, "pages": 32},
            {"file_id": 1190, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 0, "keys":53.2, "pages": 32},
            {"file_id": 1023, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 0, "keys":62.2, "pages": 32},
            {"file_id": 1094, "filename":"cmd-recv.php", "entropy": 2.5, "visits": 81.3, "referer": 1, "keys":63.5, "pages": 32},
            {"file_id": 1039, "filename":"cmd-recv.php", "entropy": 5.1, "visits": 81.3, "referer": 0, "keys":63.5, "pages": 32},
            {"file_id": 1072, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 0, "keys":63.3, "pages": 32},
            {"file_id": 1019, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 1, "keys":53.9, "pages": 32},
            {"file_id": 1033, "filename":"cmd-recv.php", "entropy": 4.5, "visits": 81.3, "referer": 0, "keys":45.7, "pages": 32},
            {"file_id": 1075, "filename":"cmd-recv.php", "entropy": 2.5, "visits": 81.3, "referer": 1, "keys":43.6, "pages": 32},
            {"file_id": 1219, "filename":"cmd-recv.php", "entropy": 2.6, "visits": 81.3, "referer": 1, "keys":41.3, "pages": 32}
        ]

        return weblogList

    
    @staticmethod
    def get_statistics_list(userId, StatisticsCount): 
        staticsList = [
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
            {"file_id": 1009, "filename":"cmd-recv.php", "text_ic": 0.02985075, "text_ent": 4.70304071, "text_lw": 30, "text_cmp":1.10447761},
        ]     

        return staticsList


    @staticmethod
    def get_fileatt_list(userId, fileattCount): 
        fileattList = [
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0},
            {"file_id": 1009, "filename":"cmd-recv.php", "file_ctime": "+0.65", "file_mtime": "+0.23", "file_mode": 755, "file_owner": 0}
        ]

        return fileattList


    @staticmethod
    def det_top_list(userId, sumCount, weblogCount, statisticsCount, fileattCount):

        topList = {
            "top_sum": FsmDetTop.get_sum_list(userId, sumCount),
            "top_weblog": FsmDetTop.get_weblog_list(userId, weblogCount),
            "top_statistics": FsmDetTop.get_statistics_list(userId, statisticsCount),
            "top_fileatt": FsmDetTop.get_fileatt_list(userId, fileattCount)
        }

        return True, topList
