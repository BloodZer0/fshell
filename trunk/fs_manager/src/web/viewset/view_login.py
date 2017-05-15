# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_登录模块


from view_base import *
from fsm_user import *


class ViewLogin(ViewBase):
    def __init__(self):
        self._rDict = {
            "username": {'n': 'userName', 't': str, 'v': None},
            "password": {'n': 'passWord', 't': str, 'v': None}
        }

    def _check_param(self):

        if not self.userName: return False, "param(username) is None!"
        if not self.passWord: return False, "param(password) is None!"

        return True, None

    def GET(self):
        return render.login()

    def _deal_login(self):
        bRet, sRet = FsmUser.login(self.userName, self.passWord)
        if not bRet:
            return bRet, sRet
        Session.set_val("username", self.userName)
        return True, sRet

    def POST(self):

        bRet, sRet = self.process(self._deal_login)
        if not bRet:
            Log.err("deal_login: %s" % (str(sRet)))
            return self.make_error(sRet)
        return self.make_response(sRet)


class ViewLogout(ViewBase):
    def GET(self):
        username = self.get_user_name()
        Session.set_val("username", None)
        Session.delete()

        return web.seeother("/login")

    def POST(self):
        return self.GET()