# -*- coding: utf-8 -*-

# project: fshell 
# author: s0nnet
# time: 2016-12-10
# desc: agent base conf

'''
LOG_LEVEL
    DEBUG   =   1
    INFO    =   2
    WARINING =  3
    ERR     =   4
    ALERT   =   5
    CLOSE   =   10
'''


import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

import ConfigParser


class AgentConf:
    
    def __init__(self):
        cfgFile = path + '/../conf/fshell_agent.conf'
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(cfgFile)


##### agent base conf

    def base_server_ip(self):
        try:
            return self.conf.get("BASE", "server_ip")
        except:
            return None
    
    def base_server_port(self):
        try:
            return self.conf.getint("BASE", "server_port")
        except:
            return None

    def base_agent_id(self):
        try:
            return self.conf.get("BASE", "agent_id")
        except:
            return None
        
    def base_dev_name(self):
        try:
            return self.conf.get("BASE", "dev_name")
        except:
            return None
        
    def base_web_enum(self):
        try:
            return self.conf.get("BASE", "web_enum")
        except:
            return None

    def base_web_dir(self):
        try:
            return self.conf.get("BASE", "web_dir")
        except:
            return None

    def base_cache_dir(self):
        try:
            return self.conf.get("BASE", "cache_dir")
        except:
            return None

    def base_log_dir(self):
        try:
            return self.conf.get("BASE", "log_dir")
        except:
            return None

    def base_log_level(self):
        try:
            return self.conf.getint("BASE", "log_level")
        except:
            return 1

    def base_log_prefix(self):
        try:
            return self.conf.get("BASE", "log_prefix")
        except:
            return ""

    def base_ctr_log(self):
        try:
            return bool(self.conf.get("BASE", "ctr_log"))
        except:
            return True


##### weblog conf

    def weblog_log_file(self):
        try:
            return self.conf.get("WEBLOG", "log_file")
        except:
            return None

    def weblog_time_sleep(self):
        try:
            return self.conf.get("WEBLOG", "time_sleep")
        except:
            return None

    def weblog_log_seek(self):
        try:
            return self.conf.get("WEBLOG", "log_seek")
        except:
            return None



"""
##### statics conf

    def statics_(self):
        try:
            return self.conf.get("STATICS", option)
        except:
            return None



##### fileatt conf

    def get_fileatt_conf(option):
        try:
            return self.conf.get("FILEATT", option)
        except:
            return None

##### danfunc conf


    def get_danfunc_conf(option):
        try:
            return self.conf.get("DANFUNC", option)
        except:
            return None

##### fuzzhash conf

    def get_fuzzhash_conf(option):
        try:
            return self.conf.get("FUZZHASH", option)
        except:
            return None

"""

class BaseConf:

    conf = AgentConf()

    AGENT_ID        =   conf.base_agent_id()
    DEV_NAME        =   conf.base_dev_name()
    WEB_ENUM        =   conf.base_web_enum()
    WEB_DIR         =   conf.base_web_dir()
    CACHE_DIR       =   conf.base_cache_dir()

    SERVER_IP       =   conf.base_server_ip()
    SERVER_PORT     =   conf.base_server_port()

    LOG_LEVEL       =   conf.base_log_level()
    LOG_DIR         =   conf.base_log_dir()
    LOG_PREFIX      =   conf.base_log_prefix()
    CTR_LOG         =   conf.base_ctr_log()
    
    
    LOG_FILE        =   conf.weblog_log_file()
    TIME_SLEEP      =   conf.weblog_time_sleep()
    LOG_SEEK        =   conf.weblog_log_seek()

    


if __name__ == "__main__":

    print BaseConf.SERVER_IP




