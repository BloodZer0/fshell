# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_日志审计


from view_base import *
from fsm_user import *


class ViewLogmanage(ViewBase):
    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("user not login!")
            return web.seeother("/login")
        return render.logmanage()

    def POST(self):
        return self.GET()


class ViewSysLogList(ViewBase):
    def __init__(self):
        self._rDict = {
            "page": {'n': 'page', 't': int, 'v': 1},
            "count": {'n': 'count', 't': int, 'v': 10}
        }

    def _check_param(self):
        bRet, sRet = super(ViewSysLogList, self)._check_param()
        if not bRet:
            return bRet, sRet
        if self.page <= 0:
            return False, "page is out of range"
        if self.count > 30 or self.count < 5:
            return False, "count is out of range"
        return True, None

    def _deal_sys_log_list_get(self):
        bRet, buId = HpsBuUser.get_user_id(self.get_user_name())
        if not bRet:
            Log.err("user_name: %s not bussiness" % (self.get_user_name()))
            return bRet, buId
        reqData = {}
        bRet, sRet = HpsBuUser.is_admin(self.get_user_name())
        if not bRet:
            Log.err("user_name: %s not bussiness" % (self.get_user_name()))
            return bRet, sRet
        if not sRet:
            reqData['userName'] = self.get_user_name()
        self.csv = get_req_qstr('csv', False)
        if self.csv is False:
            reqData['page'] = self.page
            reqData['count'] = self.count
        search = get_req_qstr('search')
        if search:
            reqData['search'] = search
        return HpsLogManager.get_log_list(buId, reqData)

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_sys_log_list_get)
        if not bRet:
            Log.err("_deal_events_actions_get: %s" % str(sRet))
            return self.make_error(sRet)
        if self.csv:
            return self.make_csv_response(sRet, 'sys_log')
        else:
            return self.make_response(sRet)


class ViewSysLogDel(ViewBase):
    def _deal_sys_log_delete(self):
        bRet, buId = HpsBuUser.get_user_id(self.get_user_name())
        if not bRet:
            Log.err("user_name: %s not bussiness" % (self.get_user_name()))
            return bRet, buId
        bRet, sRet = HpsBuUser.is_admin(self.get_user_name())
        if not bRet or not sRet:
            return False, "user have no permission"
        return HpsLogManager.delete_all_sys_log(buId)

    def POST(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_sys_log_delete)
        if not bRet:
            Log.err("deal_pot_start: %s" % (str(sRet)))
            return self.make_error(sRet)
        return self.make_response(ViewBase.RetMsg.MSG_SUCCESS)
