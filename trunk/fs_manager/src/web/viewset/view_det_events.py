# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_风险监测_事件模块


from view_base import *
from fsm_user import *
from fsm_det_events import *


class ViewDetEvents(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        render=web.template.frender("templates/detection-events.html")
        return render()

    def POST(self):
        return self.GET()


class ViewDetEventsList(ViewBase):

    def __init__(self):
        self._rDict = {
            "last_days": {'n': 'last_days', 't': int, 'v': 5}
        }

    def _check_param(self):

        if not self.last_days: return False, "param(last_days) is None!"

        return True, None

    def _deal_events_list_get(self):
        bRet, userId = FsmUser.get_user_id(self.get_user_name())
        if not bRet:
            Log.err("username: %s not bussiness" % (self.get_user_name()))
            return bRet, userId

        bRet, sRet = FsmDetEvents.det_events_list(userId, self.last_days)
        if not bRet:
            return False, sRet

        return True, sRet

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_events_list_get)
        if not bRet:
            Log.err("deal_events_list_get: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)
