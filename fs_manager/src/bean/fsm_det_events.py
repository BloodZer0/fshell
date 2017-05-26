# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web bean层_检测事件


if __name__ == "__main__":
    import sys
    import os

    sys.path.append("../base")
    sys.path.append("..")
    sys.path.append("../dao")

from fsm_cfg import *
from fs_util import *


# from fsm_result_fileatt_dao import *


class FsmDetEvents:

    @staticmethod
    def det_events_list(userId, last_days):

        events = [
            {   "title":"vrage 45%",
                "date":"2017-05-18",
                "events": [
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"webshell", "time":"21:23"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"high", "time":"21:13"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"medium", "time":"19:35"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"low", "time":"19:22"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"medium", "time":"18:13"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"low", "time":"15:29"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"low", "time":"19:22"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"webshell", "time":"14:52"}
                ]
            },
            {   "title":"vrage 51%",
                "date":"2017-05-17",
                "events": [
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"medium", "time":"23:35"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"low", "time":"22:22"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"high", "time":"19:13"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"high", "time":"14:22"}
                ]
            },
            {   "title":"vrage 31%",
                "date":"2017-05-16",
                "events": [
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"medium", "time":"23:55"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"low", "time":"21:42"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"high", "time":"11:42"}
                ]
            },
            {   "title":"vrage 22%",
                "date":"2017-05-15",
                "events": [
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"medium", "time":"16:45"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"high", "time":"12:27"}
                ]
            },
            {   "title":"vrage 15%",
                "date":"2017-05-14",
                "events": [
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"webshell", "time":"21:15"},
                    {"file_id":1002, "file_name":"cmd_recv.php", "file_risk":"high", "time":"09:42"}
                ]
            }
        ]

        return True, events



