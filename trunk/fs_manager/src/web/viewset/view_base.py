# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web框架_基本类


import web
from web_util import *
from yg_log import *
from hps_cfg import *
from hps_log_manager import *
from hps_whitelist import *
import os
import re

from xml.etree import ElementTree as ET

t_globals = dict(datestr=web.datestr, )
curPath = os.path.abspath(os.path.dirname(__file__))
render = web.template.render(curPath + '/../templates', globals=t_globals)
render._keywords['globals']['render'] = render


class Session:
    session = None

    @staticmethod
    def init(app):
        if Session.session == None:
            db = web.database(dbn='mysql', host=BaseConf.SQL_HOST, port=BaseConf.SQL_PORT,
                              user=BaseConf.SQL_USER, pw=BaseConf.SQL_PASSWD, db=BaseConf.SQL_DB)
            Session.session = web.session.Session(app, web.session.DBStore(db, 'tb_session'), initializer={})
            # Session.session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={})

    @staticmethod
    def set_val(key, val):
        Session.session[key] = val

    @staticmethod
    def get_val(key):
        if Session.session is None: return None
        if Session.session.has_key(key) is False: return None
        return Session.session.get(key)

    @staticmethod
    def delete():
        if Session.session is None: return None
        Session.session.expired()


render._keywords['globals']['session'] = Session


# 请求基础类， 完成参数提取校验
class ViewBase(object):
    class RetCode:
        T_SUCCESS = 201
        T_ERROR = 101

    class RetMsg:
        MSG_SUCCESS = "Success"

    SEPCODE_RE = re.compile(r'.*[\"\']+')

    def __init__(self):
        self._rDict = {}
        self.param = {}

    # 参数校验
    def _check_param(self):
        for name in self._rDict.keys():
            keyName = self._rDict[name]['n'] if self._rDict[name].has_key('n') else name
            value = getattr(self, keyName, None)
            if value is None:
                return False, "param(%s) is None" % (str(keyName))
            if isinstance(value, str) and self.SEPCODE_RE.match(value) is not None:
                return False, u"不允许输入特殊字符"
        return True, None

    # 日志记录
    def _log_info(self):
        self.logType = SysLogType.LOG_UNDEFINED
        self.logAttr = None

    # 参数提取
    def _get_req_param(self):
        for name in self._rDict.keys():
            valueType = str
            if self._rDict[name].has_key('t'): valueType = self._rDict[name]['t']
            defaultVal = None
            if self._rDict[name].has_key('v'): defaultVal = self._rDict[name]['v']

            value = get_req_qstr(name, defaultVal, valueType)
            if self._rDict[name].has_key('n'):
                keyName = self._rDict[name]['n']
            else:
                keyName = name
            object.__setattr__(self, keyName, value)

        return self._check_param()

    def _write_log(self, opt_result, opt_reason):
        self._log_info()
        user_name = self.get_user_name()
        remote_ip = get_client_ip()
        log_type = getattr(self, 'logType', SysLogType.LOG_UNDEFINED)
        log_attr = getattr(self, 'logAttr', None)
        if log_type == SysLogType.LOG_UNDEFINED:
            return False, ''
        return HpsLogManager.write_log(user_name, remote_ip, log_type, log_attr, opt_result, opt_reason)

    def process(self, _process=None):
        try:
            bret, sret = self._get_req_param()
            Log.info("****REQ(%s?%s): %s" % (get_req_path_info(), get_req_all_param(), sret))
            if not bret:
                return False, sret
            if _process is not None:
                bret, sret = _process()
                self._write_log(bret, sret)
            return bret, sret
        except Exception, e:
            Log.err("req(%s?%s): ERROR(%s)" % (get_req_path_info(), get_req_all_param(), traceback.format_exc()))
            return False, "req: %s ERROR(%s)" % (get_req_path_info(), str(e))

    def get_error_html(self, errInfo):
        htmlCnt = []
        htmlCnt.append("<html>")
        htmlCnt.append("<head>")
        htmlCnt.append("<title>  ERR req   </title>")
        htmlCnt.append("</head>")
        htmlCnt.append("<body>")
        htmlCnt.append("<center>")
        htmlCnt.append("</br></br></br>")
        htmlCnt.append("<h2> ERR req  </h2>")
        htmlCnt.append("</br>")
        htmlCnt.append("</br>")
        if errInfo == None: errInfo = "ERROR"
        htmlCnt.append("%s" % (str(errInfo)))
        htmlCnt.append("</center>")
        htmlCnt.append("</body>")
        htmlCnt.append("</html>")
        cnt = "".join(htmlCnt)
        return htmlCnt

    def get_json(self, retCode, retValue):
        try:
            web.header('Content-Type', 'application/json')
            if retCode == ViewBase.RetCode.T_SUCCESS:
                retJson = {"message": 'SUCCESS', "code": retCode, "result": retValue}
            else:
                retJson = {"message": retValue, "code": retCode}
            Log.info("****RESP: %s" % retJson)
            return json.dumps(retJson, encoding='utf-8')
        except Exception, e:
            Log.err("%s" % (str(e)))
            retJson = {"code": ViewBase.RetCode.T_ERROR, "message": "please hi me!"}
            return json.dumps(retJson)

    def get_result(self, retType, retCode, retValue):
        if retType == "json":
            return self.get_json(retCode, retValue)
        else:
            return retValue

    def make_paginated_response(self, result_key, result, page):
        result = self.html_encode_result(result)
        if not isinstance(page, Page):
            return self.get_json(ViewBase.RetCode.T_SUCCESS, result)
        result = {
            "count": page.item_count,
            "next": page.page_index + 1 if page.has_next else None,
            "previous": page.page_index - 1 if page.has_previous else None,
            result_key: result
        }
        return self.get_json(ViewBase.RetCode.T_SUCCESS, result)

    def make_response(self, result):
        """ 构建response对象 """
        result = self.html_encode_result(result)
        return self.get_json(ViewBase.RetCode.T_SUCCESS, result)

    def make_error(self, result):
        """构建error对象"""
        result = self.html_encode_result(result)
        return self.get_json(ViewBase.RetCode.T_ERROR, result)

    def make_csv_response(self, datas, csv_name='download'):
        def __encode_gbk(data):
            new_data = []
            for x in data:
                if isinstance(x, basestring):
                    x = x.encode("gbk", "ignore") if isinstance(x, unicode) else x
                new_data.append(x)
            return new_data

        web.header('Content-Type', 'text/csv;charset=utf-8')
        web.header('Content-Disposition', 'attachment; filename=%s.csv' % csv_name)

        writer = CSVWriter()
        for data in datas:
            data = __encode_gbk(data)
            yield writer.writerow(data)

    def make_file_response(self, file_name='download.zip'):
        base_name = os.path.basename(file_name)
        web.header('Content-Type', 'application/octet-stream;charset=utf-8')
        web.header('Content-Disposition', 'attachment; filename=%s' % base_name)

        with open(file_name, 'rb') as f:
            while True:
                content = f.read(1024)
                if content:
                    yield content
                else:
                    break

    def html_encode(self, cnt):
        if cnt is None:
            return u''

        if isinstance(cnt, str):
            cnt = cnt.decode('utf-8')
        elif not isinstance(cnt, unicode):
            cnt = unicode(cnt)

        return htmlquote(cnt)

    def html_decode(self, cnt):
        if cnt is None:
            return u''
        if isinstance(cnt, str):
            cnt = cnt.decode('utf-8')
        elif not isinstance(cnt, unicode):
            cnt = unicode(cnt)

        return htmlunquote(cnt)

    def html_encode_result(self, result):
        if isinstance(result, basestring):
            return self.html_encode(result)

        if isinstance(result, list):
            for i in range(len(result)):
                result[i] = self.html_encode_result(result[i])
            return result

        if isinstance(result, dict):
            for key in result:
                result[key] = self.html_encode_result(result[key])

            return result

        return result

    # 校验权限
    # 1、登录内网查看帐号
    def check_login(self):

        if CUR_ENV == EnvEnum.T_DEV: return True, None

        if Session.get_val("user_name") == None:
            return False, web.seeother("/login")

        return True, None

    def check_superuser_permission(self):
        bRet, userRole = self.get_user_role()
        if not bRet: return bRet, userRole

        if userRole == UserRole.COMMON_USER:
            return False

        return True

    def get_user_name(self):
        return Session.get_val("user_name")

    def get_user_role(self):
        curUser = self.get_user_name()
        return HpsBuUser.get_user_role(curUser)

    def GET(self):
        # 不能影响依赖方对数据的接收格式
        try:
            return self.process()
        except Exception, e:
            Log.err("%s" % (str(traceback.format_exc())))
            return self.get_json(ViewBase.RetCode.T_ERROR, "ERROR_ERROR")

    def POST(self):
        try:
            return self.process()
        except Exception, e:
            Log.err("%s" % (str(traceback.format_exc())))
            return self.get_json(ViewBase.RetCode.T_ERROR, "ERROR_ERROR")
