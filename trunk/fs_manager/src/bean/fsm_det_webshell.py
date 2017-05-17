# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web bean层_webshell库


if __name__ == "__main__":
    import sys
    import os

    sys.path.append("../base")
    sys.path.append("..")
    sys.path.append("../dao")

from fsm_cfg import *
from fs_util import *


# from fsm_result_fileatt_dao import *


class FsmDetWebshell:

    @staticmethod
    def det_webshell_list(userId, page, count):

        webshellList = [
            {"webshell_id": 102, "webshell_name":"db-dump.php", "webshell_md5":"3bc43416a6d3a20214a7d6428bb0e2f1", "webshell_type":u"PHP小马", "webshell_risk":5, "det_tm":"2017-05-17"},
            {"webshell_id": 103, "webshell_name":"db-dump.php", "webshell_md5":"3bc43416a6d3a20214a7d6428bb0e2f2", "webshell_type":u"PHP大马", "webshell_risk":5, "det_tm":"2017-05-17"},
            {"webshell_id": 104, "webshell_name":"db-dump.php", "webshell_md5":"3bc43416a6d3a20214a7d6428bb0e2f3", "webshell_type":u"PHP小马", "webshell_risk":5, "det_tm":"2017-05-17"},
            {"webshell_id": 105, "webshell_name":"db-dump.php", "webshell_md5":"3bc43416a6d3a20214a7d6428bb0e2f4", "webshell_type":u"PHP大马", "webshell_risk":5, "det_tm":"2017-05-16"},
            {"webshell_id": 106, "webshell_name":"db-dump.php", "webshell_md5":"3bc43416a6d3a20214a7d6428bb0e2f5", "webshell_type":u"PHP大马", "webshell_risk":5, "det_tm":"2017-05-14"},
            {"webshell_id": 107, "webshell_name":"db-dump.php", "webshell_md5":"3bc43416a6d3a20214a7d6428bb0e2f6", "webshell_type":u"PHP小马", "webshell_risk":5, "det_tm":"2017-05-15"},
            {"webshell_id": 108, "webshell_name":"db-dump.php", "webshell_md5":"3bc43416a6d3a20214a7d6428bb0e2f7", "webshell_type":u"PHP小马", "webshell_risk":5, "det_tm":"2017-05-16"},
            {"webshell_id": 109, "webshell_name":"db-dump.php", "webshell_md5":"3bc43416a6d3a20214a7d6428bb0e2f8", "webshell_type":u"PHP小马", "webshell_risk":5, "det_tm":"2017-05-13"},
            {"webshell_id": 112, "webshell_name":"db-dump.php", "webshell_md5":"3bc43416a6d3a20214a7d6428bb0e2f9", "webshell_type":u"PHP小马", "webshell_risk":5, "det_tm":"2017-05-12"},
            {"webshell_id": 113, "webshell_name":"cmd-recv.jsp", "webshell_md5":"3bc43416a6d3a20214a7d6428bb0e223", "webshell_type":u"JSP一句话马", "webshell_risk":5, "det_tm":"2017-05-14"}
        ]

        return True, webshellList

