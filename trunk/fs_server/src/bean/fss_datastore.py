# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-04
# desc: data store


from fss_proto_type import *
from fs_data_weblog_dao import *
from fs_data_statics_dao import *
from fs_data_fileatt_dao import *
from fs_data_danfunc_dao import *
from fs_data_fuzzhash_dao import *

class FsDataStore:
    
    @staticmethod
    def srote_data(reqJson):
        task_id = reqJson['task_id']
        dev_name = reqJson['dev_name']
        agent_id = reqJson['agent_id']
        msg_proto = reqJson['msg_protocol']
        msg_type = reqJson['msg_type']
        data = reqJson['data']

        if msg_proto != FsProtoProtoEnum.F_RESULT_UP:
            return False, "proto_emum error"

        if msg_type == FsProtoProtoType.F_DATA_WEBLOG:
            pass
            
        elif msg_type == FsProtoProtoType.F_DATA_STATICS:
            pass


        elif msg_type == FsProtoProtoType.F_DATA_FILEATT:
            pass




        rspData = {}


