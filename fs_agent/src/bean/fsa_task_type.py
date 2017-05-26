# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-21
# desc: 协议定义等



class FsaTaskType:
    
    F_WEBLOG    =   "web_log"
    F_STATICS   =   "statis_tics"
    F_FILEATT   =   "file_att"
    F_DANFUNC   =   "dan_func"
    F_FUZZHASH  =   "fuzz_hash"




# agent与server 通信协议定义

class FsProtoProtoEnum:
    F_RESULT_UP     = 0x01
    F_RESULT_DOWN   = 0x02
    F_CMD_REQ       = 0x03
    F_CMD_RSP       = 0x04


class FsProtoTypeEnum:

    # Agent上报数据类型(0x01 ~ 0x20)
    F_DATA_WEBLOG     =   0x01
    F_DATA_STATICS    =   0x02
    F_DATA_FILEATT    =   0x03
    F_DATA_DANFUNC    =   0x04
    F_DATA_FUZZHASH   =   0x05




