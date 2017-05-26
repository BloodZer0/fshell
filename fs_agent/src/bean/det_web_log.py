# -*- coding: UTF-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-21
# desc: detection web_log


import re
import time

if __name__ == "__main__":
    import sys
    sys.path.append("../base")

from fs_log import *
from fs_util import *
from fs_base_cfg import *
from fsa_task import *
from fsa_task_type import *


class WebLogFilter:

    """
    web log format most be this:
    if not, you will change the follow func of _format_http!
    #
    # $remote_addr [$time_local] "$request" $status $body_bytes_sent
    # "$request_body" "$http_referer" "$http_user_agent";
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
            requestBody = allGroups[5][1:-1]
            referer = allGroups[6][1:-1]
            useragent = allGroups[7][1:-1]
            
            method = request.split(" ")[0][1:]
            url = request.split(" ")[1]

            reqData = {
                "client_ip": ip,
                "time_local": time_local,
                "status": status,
                "method": method,
                "url": url,
                "req_body": requestBody,
                "referer": referer
            }

            return True, reqData

        except Exception, e:
            return False, 're match log ERR: %s' % (str(e))


    @staticmethod
    def filter(log_data):
        reqList = list()
        for line in log_data:
            bRet, reqData = WebLogFilter._format_http(line)
            if not bRet:
                return False, reqData

            Log.debug("web_log: %s" % (reqData))
            req_status = int(reqData['status'])
            req_url = reqData['url']
            file_exts = os.path.splitext(req_url)[1]

            if (req_status != 200) or (not file_exts.startswith("."+BaseConf.WEB_ENUM)):
                continue
            
            reqList.append(reqData)

        return True, reqList


class FsaTaskWeblog:

    def __init__(self):
        self.log_file = BaseConf.LOG_FILE
        self.time_wait = BaseConf.TIME_WAIT
        self.log_seek = "%s/%s" % (BaseConf.CACHE_DIR, BaseConf.LOG_SEEK)
    

    def _read_seek(self):
        if not os.path.exists(self.log_seek):
            f = open(self.log_seek, "w")
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
        f.write(str(seek))
        f.close()


    def start_task(self):
        while True:
            time.sleep(self.time_wait)

            file_seek = self._read_seek()
            f = open(self.log_file, 'r')
            f.seek(file_seek)
            log_content = f.readlines()
            file_seek_end = f.tell()
            f.close()
            
            if len(log_content) == 0:
                Log.info("no increase of web log, wait %s(s)" %(self.time_wait))
                continue
    
            bRet, logData = WebLogFilter.filter(log_content)
            if not bRet or len(logData) == 0:
                Log.err(logData)
                continue

            Log.debug("write seek: %d" % (file_seek_end))
            self._write_seek(file_seek_end)
            Log.debug("filter log succ, len: %d" % (len(logData)))
            bRet, sRet = FsaTaskClient.report_task(FsaTaskType.F_WEBLOG, FsaTaskStatus.T_FINISH, logData)
            if not bRet:
                Log.err("Report web log ERR: %s" % (sRet))
   
            



if __name__ == "__main__":

    tk = FsaTaskWeblog()
    tk.start_task()




