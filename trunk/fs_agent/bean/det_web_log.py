# -*- coding: UTF-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-21
# desc: detection web_log


import re
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
    def _generate_re_cpl():

        ipP = r"?P<ip>[\d.]*"
        
        timeP = r"""?P<time>\[
                [^\[\]]*
                \]
                """

        requestP = r"""?P<request>\"
                    [^\"]*
                    \"
                    """
        
        statusP = r"?P<status>\d+"

        bodyBytesSentP = r"?P<bodyByteSent>\d+"
        
        requestBodyP = r"""?P<requestBody>\"
                        [^\"]*
                        \"
                        """

        refererP = r"""?P<referer>\"
                    [^\"]*
                    \"
                    """

        userAgentP = r"""?P<userAgent>\"
                    [^\"]*
                    \"
                    """

        re_cpl = re.compile(r"(%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)" % (ipP, timeP, requestP, statusP, bodyBytesSentP, requestBodyP, refererP, userAgentP), re.VERBOSE)

        return re_cpl


    @staticmethod
    def _format_http(line):
        try:
            ReCpl = WebLogFilter._generate_re_cpl()
            matchs = ReCpl.match(line.strip())
            if  not matchs:
                return False, 're match log ERR'

            allGroups = matchs.groups()
            
            ip = allGroups[0]
            time_local = allGroups[1]
            request = allGroups[2]
            status = allGroups[3]
            bodyByteSent = allGroups[4]
            requestBody = allGroups[5]
            referer = allGroups[6]
            useragent = allGroups[7]
            
            method = request.split(" ")[0]
            url = request.split(" ")[1]

            reqData = {
                "ip": ip,
                "time": time_local,
                "status": status,
                "method": method,
                "url": url,
                "request_body": requestBody,
                "referer": referer
            }

            return True, reqData

        except:
            return False, 're match log ERR'


    @staticmethod
    def filter(log_data):
        reqList = list()
        for line in log_data:
            bRet, reqData = WebLogFilter._format_http(line)
            if not bRet:
                return False, 'Filter log ERR'

            req_status = reqData['status']
            req_url = reqData['url']
            file_exts = os.path.splitext(req_url)[1]

            if (status != 200) or (not file_exts.startswith("."+BaseConf.WEB_ENUM)):
                continue
            
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
