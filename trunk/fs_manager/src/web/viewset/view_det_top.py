# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_风险监测_TOP事件


from view_base import *
from fsm_user import *
from fsm_det_top import *


class ViewDetTop(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        render=web.template.frender("templates/detection-top.html")
        return render()

    def POST(self):
        return self.GET()


class ViewDetTopList(ViewBase):

    def __init__(self):
        self._rDict = {
            "top_count": {'n': 'top_count', 't': int, 'v': 12}
        }

    def _check_param(self):

        if not self.top_count: return False, "param(top_count) is None!"

        return True, None

    def _deal_top_list_get(self):
        bRet, userId = FsmUser.get_user_id(self.get_user_name())
        if not bRet:
            Log.err("username: %s not bussiness" % (self.get_user_name()))
            return bRet, userId

        bRet, sRet = FsmDetTop.det_top_list(userId, self.top_count)
        if not bRet:
            return False, sRet

        return True, sRet

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_top_list_get)
        if not bRet:
            Log.err("deal_top_list_get: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)