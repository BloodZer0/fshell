# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-04
# desc: data store


if __name__ == "__main__":
    import sys
    sys.path.append("..")
    sys.path.append("../base")

from fs_proto_type import *
from fss_data_weblog import *
from fss_data_statics import *
from fss_data_fileatt import *
from fss_data_danfunc import *
from fss_data_fuzzhash import *

class FssDataStore:
    
    @staticmethod
    def store_data(reqJson):
        task_id = reqJson['task_id']
        dev_name = reqJson['dev_name']
        agent_id = reqJson['agent_id']
        msg_proto = reqJson['msg_protocol']
        msg_type = reqJson['msg_type']
        data = reqJson['data']

        if msg_proto != FsProtoProtoEnum.F_RESULT_UP:
            return False, "proto_emum error"

        if msg_type == FsProtoTypeEnum.F_DATA_WEBLOG:
            bRet, sRet = FssWebLog.insert_node(agent_id, data)
            if not bRet: return False, sRet

        elif msg_type == FsProtoTypeEnum.F_DATA_STATICS:
            bRet, sRet = FssStatics.insert_node(agent_id, data)
            if not bRet: return False, sRet

        elif msg_type == FsProtoTypeEnum.F_DATA_FILEATT:
            bRet, sRet = FssFileAtt.insert_node(agent_id, data)
            if not bRet: return False, sRet

        elif msg_type == FsProtoTypeEnum.F_DATA_DANFUNC:
            bRet, sRet = FssDanFunc.insert_node(agent_id, data)
            if not bRet: return False, sRet

        elif msg_type == FsProtoTypeEnum.F_DATA_FUZZHASH:
            bRet, sRet = FssFuzzHash.insert_node(agent_id, data)
            if not bRet: return False, sRet
        
        else:
            return False, "msg_type error"


        rspData = {
            "proto_emum": FsProtoProtoEnum.F_RESULT_DOWN,
            "proto_type": msg_type,
            "data": ""
        }

        return True, rspData


if __name__ == "__main__":

    reqJson_web_log = {
        "task_id": "123456qwertyuiop",
        "dev_name": "websrv_debain_8",
        "agent_id": 1002,
        "msg_protocol": 0x01,
        "msg_type": 0x01,
        "data": {
            "client_ip": "222.24.62.100",
            "time_local": "[12/01/2016 +8000]",
            "method": "POST",
            "url": "/user/add/userinfo.php",
            "req_body": "uid=1004&task=show",
            "referer": "/index.html"
        }
    }

    reqJson_statics = {
        "task_id": "qwe32rwrerwqeqw",
        "dev_name": "websrv_ubuntu_1",
        "agent_id": 1003,
        "msg_protocol": 0x01,
        "msg_type": 0x02,
        "data": {
            "filename": "/user/show.php",
            "text_ic": "0.562345432",
            "text_ent": "0.934212",
            "text_lw": 1234,
            "text_cmp": "0.7322"
        }
    }

    reqJson_fileatt = {
        "task_id": "rter324g4645643",
        "dev_name": "websrv_redhat5",
        "agent_id": 1004,
        "msg_protocol": 0x01,
        "msg_type":  0x03,
        "data": {
            "filename": "/admin/order/list.php",
            "file_ctime": "2016-12-23 12:11:09",
            "file_mtime": "2017-23-23 22:22:01",
            "file_mode": 755,
            "file_owner": "1000.1000",
        }
    }

    reqJson_danfunc = {
        "task_id": "vdgdfgd3453657",
        "dev_name": "websrv_redhat8",
        "agent_id": 1005,
        "msg_protocol": 0x01,
        "msg_type": 0x04,
        "data": {
            "filename": "/admin/user/manager.php",
            "weight_sum": 104,
            "functions": "mysql_connect, cmd_exec, get_user, len",
        }
    }

    reqJson_funzhash = {
        "task_id": "gfhdf567hrthgt",
        "dev_name": "websrv_redhat2",
        "agent_id": 1006,
        "msg_protocol": 0x01,
        "msg_type": 0x05,
        "data": {
            "filename": "admin/useradd/shell.php",
            "fuzz_hash": "F945M340:5543534523495U5343:9F8R3C34W2"
        }
    }

    print FssDataStore.store_data(reqJson_funzhash)


