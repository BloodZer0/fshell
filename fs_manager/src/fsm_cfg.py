# -*- coding: utf--8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: fs_manager conf


from fs_base_cfg import *

class EnvEnum:
    T_DEV       =   "dev"
    T_ONLINE    =   "online"

    
CUR_ENV         =   EnvEnum.T_DEV

if CUR_ENV ==  EnvEnum.T_DEV:
    
    BaseConf.IS_CTR_LOG     =   True
    BaseConf.LOG_LEVEL      =   1
    BaseConf.SQL_HOST       =   "222.24.xx.xx"
    BaseConf.SQL_PORT       =   3306
    BaseConf.SQL_USER       =   "fshell_user"
    BaseConf.SQL_PASSWD     =   "fshell_passwd"
    BaseConf.SQL_DB         =   "fshell_db"
    
    SERVER_IP               =   "127.0.0.1"
    SERVER_PORT             =   8000

else:
    BaseConf.IS_CTR_LOG     =   True
    BaseConf.LOG_LEVEL      =   1
    BaseConf.SQL_HOST       =   "127.0.0.1"
    BaseConf.SQL_PORT       =   3306
    BaseConf.SQL_USER       =   "xxxx"
    BaseConf.SQL_PASSWD     =   "xxx"
    BaseConf.SQL_DB         =   "db_fshell"

    SERVER_IP        =   "127.0.0.1"
    SERVER_PORT      =   8000
    

# with local cfg, so do not modify the file when test in local env
if os.path.exists(os.path.join(os.path.dirname(__file__), 'fsm_local_cfg.py')):
    from fsm_local_cfg import *
