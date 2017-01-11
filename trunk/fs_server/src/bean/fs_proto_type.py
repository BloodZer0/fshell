# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-11
# desc: 通信协议定义


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


    # 服务端命令下发(0x30 ~ 0x60)
    F_CMD_OK   =   0x30
