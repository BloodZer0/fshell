# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_登录模块


from view_base import *
from hps_user_dao import *


class ViewLogin(ViewBase):
    def __init__(self):
        self._rDict = {
            "user_name": {'n': 'userName', 't': str, 'v': None},
            "password": {}
        }

    def _check_param(self):

        if not self.userName: return False, "param(user_name) is None!"
        if not self.password: return False, "param(password) is NOne!"

        return True, None

    def _log_info(self):
        self.logType = SysLogType.LOG_LOGIN_SUCCESS
        self.logAttr = [{'key': u'用户名', 'val': self.userName}]

    def GET(self):
        return render.login()

    def _deal_login(self):
        bRet, sRet = HpsBuUser.login(self.userName, self.password)
        if not bRet:
            return bRet, sRet
        Session.set_val("user_name", self.userName)
        return True, sRet

    def POST(self):

        bRet, sRet = self.process(self._deal_login)
        if not bRet:
            Log.err("deal_login: %s" % (str(sRet)))
            return self.make_error(sRet)
        return self.make_response(sRet)
        # return web.seeother("/dashboard.html")


class ViewLogout(ViewBase):
    def GET(self):
        user_name = self.get_user_name()
        Session.set_val("user_name", None)
        Session.delete()
        HpsLogManager.write_log(user_name, get_client_ip(), SysLogType.LOG_LOGOUT_SUCCESS, None, True, '')
        return web.seeother("/login")

    def POST(self):
        return self.GET()


if __name__ == "__main__":

    def test_login():
        Session.session = {}
        viewLogin = ViewLogin()
        viewLogin.userName = 'moresec'
        viewLogin.password = 'test'
        bRet, sRet = viewLogin._deal_login()
        if not bRet:
            Log.err("test_case ERR! %s" % (str(sRet)))
        else:
            Log.info("test_case SUCCESS!")


    test_login()
