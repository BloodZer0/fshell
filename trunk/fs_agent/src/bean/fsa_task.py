# -*- coding: utf-8 -*-

# project: fshll
# author: s0nnet
# time: 2016-12-12
# desc: 任务接收/上报模块

import sys
import uuid

sys.path.append("../base")
sys.path.append("../net")

from fs_time import *
from fs_base_cfg import *
from fsa_net import *
from fsa_task_type import *


class FsaTaskStatus:
    T_RUN       =   "run"
    T_FAIL      =   "fail"
    T_FINISH    =   "finish"
    
    statusList = [T_RUN, T_FAIL, T_FINISH]
    
    @staticmethod
    def valid_check(status):
        for st in FsaTaskStatus.statusList:
            if st == status: 
                return True
        
        return False

    

class FsaTaskClient:

    @staticmethod
    def _send_pkt(taskData):
        reqJson = {}
        reqJson['task_id'] = uuid.uuid1().get_hex()
        reqJson['dev_name'] = BaseConf.DEV_NAME
        reqJson['agent_id'] = BaseConf.AGENT_ID
        reqJson['msg_protocol'] = FsProtoProtoEnum.F_RESULT_UP
        reqJson['msg_type'] = FsProtoTypeEnum.F_DATA_WEBLOG
        reqJson['data'] = taskData

        return FsaNet.send_req(reqJson)


    @staticmethod
    def _get_task():

        now_tm = get_cur_time()

        time_dict = {
            "statics": BaseConf.STATICS_RUN_TIME,
            "fileatt": BaseConf.FILEATT_RUN_TIME,
            "danfunc": BaseConf.DANFUNC_RUN_TIME,
            "fuzzhash": BaseConf.FUZZHASH_RUN_TIME
        }
        
        print time_dict

        for key,val in time_dict.items():
            for tm in val:
                if tm == now_tm:
                    return True, key


        # debug....
        return True, 'statics'

        return True, None

    
    @staticmethod
    def get_task():
        bRet, taskType = FsaTaskClient._get_task()
        if taskType is None:
            return True, None

        return True, taskType
    
    
    @staticmethod
    def report_task(taskType, taskStatus, taskData):
        if FsaTaskStatus.valid_check(taskStatus) == False:
            Log.err("status(%d) is not valid" %(taskStatus))
            return False, "status(%d) is not valid" %(taskStatus)
        
        if taskData == None: taskData = taskStatus
        
        # 预留　结果本地缓存模块
        #
        #
        #
        #
        #

        return FsaTaskClient._send_pkt(taskData)


if __name__ == "__main__":
    
    bRet, taskType = FsaTaskClient.get_task()
    
    print bRet, taskType
    
    #print FsaTaskClient.report_task("web_log", FsaTaskStatus.T_RUN, "hi,s0nnet!")
        
