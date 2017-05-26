# -*- coding: utf-8 -*- 

#
# this a example using re to format web log.
# here is the standard web log:
# ```
# $remote_addr [$time_local] "$request" $status $body_bytes_sent
# "$request_body" "$http_referer" "$http_user_agent";
# ```


import os
import re


ipP = r"?P<ip>[\d.]*";
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



referP = r"""?P<refer>\"
        [^\"]*
        \"
        """

userAgentP = r"""?P<userAgent>\"
            [^\"]*
            \"
            """



LogP = re.compile(r"(%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)" % (ipP, timeP, requestP, statusP, bodyBytesSentP, requestBodyP, referP, userAgentP), re.VERBOSE)


f = open("standard_web_log.log")

 
for line in f.readlines():
    matchs = LogP.match(line.strip())

    if matchs != None:
        allGroups = matchs.groups()
        print 'ip>>>', allGroups[0]
        print 'time>>>', allGroups[1]
        print 'request>>>', allGroups[2]
        print 'status>>>', allGroups[3]
        print 'bodyByteSent:', allGroups[4]
        print 'requestBody:', allGroups[5]
        print 'refer:', allGroups[6]
        print 'useragent:', allGroups[7]


    else:
        print 'error'

f.close()






