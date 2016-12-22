# -*- coding: UTF-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-21
# desc: detection web_log


import time
from fs_base_cfg import *
from fsa_task import *
from fsa_task_type import *

class WebLogFilter:

    """
    web log format most be this:
    if not, you will change the follow func of _format_http!
    # 
    # $remote_addr - [$time_local] - "$request" - $status -
    # $body_bytes_sent - "$request_body" - "$http_referer"
    #
    """

    @staticmethod
    def _format_http(line, option):
        try:
            row = line.split("-")

            if option == 'status':
                status = row[3].strip()
                return int(status)

            elif option == 'time':
                time_local = row[1].strip()
                time_local = time_local[1:20]
                tm = time.strptime(time_local, "%d/%b/%y:%H:%M:%S")
                return int(time.mktime(tm))

            elif option == 'referer':
                referer = row[6].replace('"', '')


            else:
                req = row[2].strip()
                req = req.replace('"', '')
                method = req.split(" ")[0]
                
                if option == 'uri':
                    url = req.split(" ")[1]
                    uri_re = ''
                    return uri_re
                
                if option == 'data':
                    if method == 'POST':
                        return row[5].replace('"', '')

                    elif method == "GET":



                    else:
                        pass
                
                return None

        except:
            return None


    @staticmethod
    def filter(log_data):
        
        reqList = list()
        for line in log_data:
            req_status = WebLogFilter._get_http_status(line)
            req_uri = WebLogFilter._get_http_uri(line)
            if (status != 200) or (uri.split(".")[-1] != BaseConf.WEB_ENUM):
                continue
            
            reqData = {
                "req_status": req_status,
                "req_uri": req_uri,
                "req_time": WebLogFilter._get_http_time(line),
                "req_data": WebLogFilter._get_http_data(line),
                "req_refer": WebLogFilter._get_http_refer(line)
            }
            reqList.append(reqData)

        return True, reqList


class FsaTaskWeblog:

    def __init__(self):
        self.log_file = BaseConf.LOG_FILE
        self.time_sleep = BaseConf.TIME_SLEEP
        self.log_seek = "%s/%s" % (BaseConf.CACHE_DIR, BaseConf.LOG_SEEK)
    

    def _read_seek(self):
        if not os.path.exists(self.log_seek):
            f = open(self.log_seek)
            f.close()
            return 0

        f = open(self.log_seek, 'r')
        result = f.read()
        f.close()
        if not result:
            return 0

        return long(result)


    def _write_seek(self, seek):
        f = open(self.log_seek, 'w')
        f.write(seek)
        f.close()


    def start_task(self):
        while True:
            file_seek = self._read_seek(self.log_seek)
            f = open(self.log_file, 'r')
            f.seek(file_seek)
            log_content = f.readlines()
            offset = f.tell()
            f.close()
            
            bRet, logData = WebLogFilter.filter(log_content)
            if not bRet:
                Log.err("Filter web log ERR: %s" % (logData))
                offset = 0

            file_seek += offset 
            self._write_seek(file_seek)

            bRet, sRet = FsaTaskClient.report_task(FsaTaskType.F_WEBLOG, FsaTaskStatus.T_FINISH, logData)
            if not bRet:
                Log.err("Report web log ERR: %s" % (sRet))
                #
            
            time.sleep(self.time_sleep)    
