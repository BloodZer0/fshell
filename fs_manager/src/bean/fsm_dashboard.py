# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-15
# desc: web bean层_Dashboard


if __name__ == "__main__":
    import sys
    import os

    sys.path.append("../base")
    sys.path.append("..")
    sys.path.append("../dao")

from fsm_cfg import *
from fs_util import *
from fsm_user_dao import *


class FsmDashboard:

    @staticmethod
    def det_charts(userId):

        chartsInfo = {
            "flotDashSales1Data": {"data": [["Jan", 140],["Feb", 130],["Mar", 1930],["Apr", 2409],
                                            ["May", 2204],["Jun", 3208],["Jul", 2712],["Aug", 1895]],
                                   "color": "#0088cc"
                                },
            "flotDashSales2Data": {"data": [["Jan", 2],["Feb", 24],["Mar", 211],["Apr", 340],
                                        ["May", 320],["Jun", 389],["Jul", 170],["Aug", 94]],
                                  "color": "#e36159"
                                },
            "flotDashSales3Data": {"data": [["Jan", 34],["Feb", 45],["Mar", 95],["Apr", 340],
                                        ["May", 182],["Jun", 120],["Jul", 142],["Aug", 78]],
                                  "color" : "#734ba9"
                                }
        }

        return True, chartsInfo


    @staticmethod
    def det_statistics(userId):

        statiStics = {
            "webshell_val": 18,
            "danger_val": 35,
            "site_num": 3,
            "agent_num": 3,
            "webshell_num": 25,
            "lib_num": 1388,
            "danger_num": 120 
        }

        return True, statiStics


    @staticmethod
    def det_top_charts(userId):

        topCharts = [
            {
                "data": [
                        [0, 170],[1, 169],[2, 173],[3, 188],[4, 147],[5, 113],[6, 128],[7, 169],[8, 173],[9, 128],[10, 128]],
                "label": u"文本属性",
                "color": "#0088cc",
                "class": 1
            },
            {
                "data": [
                        [0, 115],[1, 124],[2, 112],[3, 122],[4, 109],[5, 84],[6, 101],[7, 145],[8, 139],[9, 102],[10, 112]],
                "label": u"高危函数",
                "color": "#2baab1",
                "class": 2
            },
            {
                "data": [
                        [0, 70],[1, 69],[2, 73],[3, 85],[4, 47],[5, 13],[6, 28],[7, 69],[8, 73],[9, 28],[10, 25]],
                "label": u"统计学",
                "color": "#734ba9",
                "class": 3
            }
        ]

        return True, topCharts


    @staticmethod
    def det_log_charts(userId):

        return True, 'has not compled!'


    @staticmethod
    def det_top_webshell(userId):

        topWebshell = [
            {"id": 1, "file":"include_smart_connect.php", "status": 3, "progress": 95.3, "file_id": 1002},
            {"id": 2, "file":"include_smart_connect.php", "status": 3, "progress": 93.5, "file_id": 1002},
            {"id": 3, "file":"include_smart_connect.php", "status": 3, "progress": 92.6, "file_id": 1002},
            {"id": 4, "file":"include_smart_connect.php", "status": 3, "progress": 91.9, "file_id": 1002},
            {"id": 5, "file":"include_smart_connect.php", "status": 3, "progress": 91.8, "file_id": 1002},
            {"id": 6, "file":"include_smart_connect.php", "status": 2, "progress": 89.3, "file_id": 1002},
            {"id": 7, "file":"include_smart_connect.php", "status": 2, "progress": 85.8, "file_id": 1002},
            {"id": 8, "file":"include_smart_connect.php", "status": 2, "progress": 83.9, "file_id": 1002},
            {"id": 9, "file":"include_smart_connect.php", "status": 2, "progress": 82.3, "file_id": 1002},
            {"id": 10, "file":"include_smart_connect.php", "status": 1, "progress": 75.3, "file_id": 1002},
            {"id": 11, "file":"include_smart_connect.php", "status": 1, "progress": 72.3, "file_id": 1002},
            {"id": 12, "file":"include_smart_connect.php", "status": 1, "progress": 70.6, "file_id": 1002},
            {"id": 13, "file":"include_smart_connect.php", "status": 1, "progress": 65.3, "file_id": 1002},
            {"id": 14, "file":"include_smart_connect.php", "status": 1, "progress": 62.5, "file_id": 1002},
            {"id": 15, "file":"include_smart_connect.php", "status": 1, "progress": 55.8, "file_id": 1002}
        ]

        return True, topWebshell


    @staticmethod
    def det_sys_status(userId):

        sysStatus = {
            "net": [5, 6, 8, 2, 0, 4 , 2, 4, 2, 1, 4 , 5, 7, 2, 0, 4],
            "cpu": 45,
            "mem": [15, 16, 17, 19, 10, 15, 13, 12, 12, 14, 16, 17]
        }

        return True, sysStatus


    @staticmethod
    def det_agents(userId):

        agentOnline = [

            {"agent_id":1000, "agent_name":"agent_test001", "agent_ip":"222.24.62.48", "agent_type":"apache", "update_tm":"2017-05-15 12:23:45"},
            {"agent_id":1001, "agent_name":"agent_test002", "agent_ip":"192.168.230.112","agent_type":"nginx", "update_tm":"2017-05-15 12:23:45"},
            {"agent_id":1002, "agent_name":"agent_test003", "agent_ip":"192.168.230.118","agent_type":"nginx" ,"update_tm":"2017-05-15 12:23:45"}
        ]

        return True, agentOnline



