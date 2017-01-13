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

    def weblog_time_wait(self):
        try:
            return self.conf.getint("WEBLOG", "time_wait")
        except:
            return 3

    def weblog_log_seek(self):
        try:
            return self.conf.get("WEBLOG", "log_seek")
        except:
            return "web_log_seek.tmp"


##### statics conf

    def statics_run_time(self):
        try:
            return list(set(self.conf.get("STATICS", "run_time").split(",")))
        except:
            return None

    def statics_smallest_filesize(self):
        try:
            return self.conf.getint("STATICS", "smallest_filesize")
        except:
            return 30
    
    def statics_result_output(self):
        try:
            return self.conf.get("STATICS", "result_output")
        except:
            return "statistics_output.csv"

    def statics_scan_file_ext(self):
        try:
            return self.conf.get("STATICS", "scan_file_ext")
        except:
            return None



##### fileatt conf

    def fileatt_run_time(self):
        try:
            return list(set(self.conf.get("FILEATT", "run_time").split(",")))
        except:
            return None

    def fileatt_result_output(self):
        try:
            return self.conf.get("FILEATT", "result_output")
        except:
            return "fileatt_output.csv"

    def fileatt_scan_file_ext(self):
        try:
            return self.conf.get("FILEATT", "scan_file_ext")
        except:
            return None



##### danfunc conf

    def danfunc_run_time(self):
        try:
            return list(set(self.conf.get("DANFUNC", "run_time").split(",")))
        except:
            return None

    def danfunc_result_output(self):
        try:
            return self.conf.get("DANFUNC", "result_output")
        except:
            return "danfunc_output.csv"

    def danfunc_scan_file_ext(self):
        try:
            return self.conf.get("DANFUNC", "scan_file_ext")
        except:
            return None



##### fuzzhash conf

    def fuzzhash_run_time(self):
        try:
            return list(set(self.conf.get("FUNZHASH", "run_time").split(",")))
        except:
            return None

    def fuzzhash_result_output(self):
        try:
            return self.conf.get("FUZZHASH", "result_output")
        except:
            return "funzhash_output.csv"

    def fuzzhash_scan_file_ext(self):
        try:
            return self.conf.get("FUZZHASH", "scan_file_ext")
        except:
            return None




class BaseConf:

    conf = AgentConf()

    # define base config
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
    
    
    # define weblog config
    LOG_FILE        =   conf.weblog_log_file()
    TIME_WAIT       =   conf.weblog_time_wait()
    LOG_SEEK        =   conf.weblog_log_seek()

    # define statics config
    STATICS_RUN_TIME        =   conf.statics_run_time()
    SMALLEST_FILESIZE       =   conf.statics_smallest_filesize()
    STATICS_RESULT          =   conf.statics_result_output()
    STATICS_SCAN_FILE_EXT   =   conf.statics_scan_file_ext()

    # define file attribute config
    FILEATT_RUN_TIME        =   conf.fileatt_run_time()
    FILEATT_RESULT          =   conf.fileatt_result_output()
    FILEATT_SCAN_FILE_EXT   =   conf.fileatt_scan_file_ext()


    # define danger func config
    DANFUNC_RUN_TIME        =   conf.danfunc_run_time()
    DANFUNC_RESULT          =   conf.danfunc_result_output()
    DANFUNC_SCAN_FILE_EXT   =   conf.danfunc_scan_file_ext()


    # define fuzzy hash config
    FUNZHASH_RUN_TIME       =   conf.fuzzhash_run_time() 
    FUNZHASH_RESULT         =   conf.fuzzhash_result_output() 
    FUZZHASH_SCAN_FILE_EXT  =   conf.fuzzhash_scan_file_ext()

    


if __name__ == "__main__":

    print BaseConf.SERVER_IP




