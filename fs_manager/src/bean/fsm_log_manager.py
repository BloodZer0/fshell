# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-15
# desc: web bean层_日志管理


from web.utils import *
from fsm_sys_log_dao import *
from fsm_user import *


class SysLogType:
    LOG_LOGIN_SUCCESS = u"用户登录"
    LOG_LOGOUT_SUCCESS = u"用户注销"
    LOG_MODIFY_PLUGIN = u"修改密巢配置"
    LOG_CREATE_PLUGIN = u'新建密巢'

    LOG_UNDEFINED = u'未定义'


class FsmLogManager:

    @staticmethod
    def write_log(userName, remoteAddr, logType, logAttr, logResult, logReason):
        bRet, userId = FsmUser.get_user_id(userName)
        if not bRet:
            Log.err("write log failed.")
            return bRet, userId

        logReason = logReason if logResult is False else u''
        logResult = u'操作成功' if logResult is True else u'操作失败'
        try:
            if logAttr is not None:
                logAttr = json.dumps(logAttr, encoding='utf-8')
            else:
                logAttr = u''
        except Exception, e:
            logAttr = u''

        bRet, sRet = FsmSysLogDao.insert_node(userId, userName, remoteAddr, logType, logAttr, logResult, logReason)
        if not bRet:
            Log.err("user (%s) write sys log failed." % userId)
            return bRet, sRet
        return True, sRet


    @staticmethod
    def get_log_list(userId, reqData=None):
        params = storage(reqData or dict())
        userName = params.get('userName', None)
        page = params.get('page', None)
        count = params.get('count', None)
        search = params.get('search', None)
        if page is None and count is None:
            bRet, sRet = HpsSysLogDao.query_nodes_by_user(userId, userName)
            if not bRet:
                Log.err("get sys log list ERR: %s" % str(sRet))
                return bRet, sRet
            log_list = []
            title = [u'审计时间', u'登录用户', u'登录IP', u'审计事件', u'审计详情']
            log_list.append(title)
            for item in sRet:
                log_detail = u'事件结果：%s ' % item['log_result']
                if item['log_reason']:
                    log_detail += u'失败原因：%s ' % item['log_reason']
                log_detail += u'事件属性：'
                log_attr = safe_json_loads(item['log_attr']) or []
                for attr in log_attr:
                    log_detail += u'%s(%s) ' % (attr['key'], attr['val'])
                log_info = [safe_datetime_to_str(item['insert_tm']), item['referee'], item['remote_addr'],
                            safeunicode(item['log_content']), safeunicode(log_detail)]
                log_list.append(log_info)
            return True, log_list
        else:
            bRet, total = HpsSysLogDao.query_nodes_count_by_user(userId, userName, search)
            if not bRet:
                Log.err("get log list ERR: %s" % str(total))
            paginated = Page(total, page or 1, count or 10)
            bRet, sRet = HpsSysLogDao.query_nodes_by_user(userId, userName, paginated.offset, paginated.limit, search)
            if not bRet:
                Log.err("get log list ERR: %s" % str(sRet))
                return bRet, sRet
            log_list = []
            for item in sRet:
                log_info = dict()
                log_info['login_user'] = item['referee']
                log_info['login_ip'] = item['remote_addr']
                log_info['operation'] = item['log_content']
                log_info['create_tm'] = safe_datetime_to_str(item['insert_tm'])
                log_info['opt_result'] = item['log_result']
                log_info['opt_reason'] = item['log_reason']
                log_info['opt_attr'] = safe_json_loads(item['log_attr']) or []
                log_list.append(log_info)
            return True, HpsLogManager._page_data(log_list, 'logs', paginated)

    @staticmethod
    def delete_all_sys_log(userId):
        bRet, sRet = HpsSysLogDao.del_nodes_by_user(userId)
        if not bRet:
            Log.err("delete all user (%s) sys log ERR: %s" % (str(userId), str(sRet)))
            return bRet, sRet
        return bRet, sRet
