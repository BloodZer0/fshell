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
    def det_charts():

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
    def det_statistics():

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














