# -*- coding: UTF-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-11
# desc: srv manager


from fss_cfg import *
from fss_net import *
from fss_srv_base import *
from fss_proto_type import *
from fss_datastore import *


class FsManagerSrv:
    
    def __init__(self):
        self.ip      =   SERVER_IP
        self.port    =   SERVER_PORT
        self.mode    =   FsNetMode.T_SYN_MODE
        
    
    def deal_pkg(self, session, reqJson):
        
        bRet = FsContentProto.check_valid(reqJson)
        if not bRet:  return False, ""
       
        Log.debug("recv_data: %s" % (reqJson))

        # data store
        bRet, rspData = FsDataStore.store_data(reqJson)
        if not bRet:
            return False, ""

        rspEnum = rspData['proto_emum']
        rspProto = rspData['proto_type']
        rspData = rspData['data']
       
        return FsContentProto.response_packet(session, reqJson, rspEnum, rspProto, rspData)
