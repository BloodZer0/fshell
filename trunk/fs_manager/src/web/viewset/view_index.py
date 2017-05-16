# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_dashborad


from view_base import *
from fsm_user import *
from fsm_dashboard import *


class ViewIndex(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        return render.index()

    def POST(self):
        return self.GET()


class ViewDashboardCharts(ViewBase):

    def _deal_charts_get(self):
        bRet, userId = FsmUser.get_user_id(self.get_user_name())
        if not bRet:
            Log.err("username: %s not bussiness" % (self.get_user_name()))
            return bRet, userId

        bRet, sRet = FsmDashboard.det_charts(userId)
        if not bRet:
            return False, sRet

        return True, sRet

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_charts_get)
        if not bRet:
            Log.err("deal_charts_get: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)


class ViewDashboardStatistics(ViewBase):

    def _deal_statistics_get(self):
        bRet, userId = FsmUser.get_user_id(self.get_user_name())
        if not bRet:
            Log.err("username: %s not bussiness" % (self.get_user_name()))
            return bRet, userId

        bRet, sRet = FsmDashboard.det_statistics(userId)
        if not bRet:
            return False, sRet

        return True, sRet    

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_statistics_get)
        if not bRet:
            Log.err("deal_statistics_get: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)


class ViewDashboardTopsCharts(ViewBase):

    def _deal_top_charts_get(self):
        bRet, userId = FsmUser.get_user_id(self.get_user_name())
        if not bRet:
            Log.err("username: %s not bussiness" % (self.get_user_name()))
            return bRet, userId

        bRet, sRet = FsmDashboard.det_top_charts(userId)
        if not bRet:
            return False, sRet

        return True, sRet    

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_top_charts_get)
        if not bRet:
            Log.err("deal_top_charts_get: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)


class ViewDashboardLogCharts(ViewBase):

    def _deal_log_charts_get(self):
        bRet, userId = FsmUser.get_user_id(self.get_user_name())
        if not bRet:
            Log.err("username: %s not bussiness" % (self.get_user_name()))
            return bRet, userId

        bRet, sRet = FsmDashboard.det_log_charts(userId)
        if not bRet:
            return False, sRet

        return True, sRet    

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_log_charts_get)
        if not bRet:
            Log.err("deal_log_charts_get: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)


class ViewDashboardTopsWebshell(ViewBase):

    def _deal_top_webshell_get(self):
        bRet, userId = FsmUser.get_user_id(self.get_user_name())
        if not bRet:
            Log.err("username: %s not bussiness" % (self.get_user_name()))
            return bRet, userId

        bRet, sRet = FsmDashboard.det_top_webshell(userId)
        if not bRet:
            return False, sRet

        return True, sRet    

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_top_webshell_get)
        if not bRet:
            Log.err("deal_top_webshell_get: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)


class ViewDashboardSysStatus(ViewBase):

    def _deal_sys_status_get(self):
        bRet, userId = FsmUser.get_user_id(self.get_user_name())
        if not bRet:
            Log.err("username: %s not bussiness" % (self.get_user_name()))
            return bRet, userId

        bRet, sRet = FsmDashboard.det_sys_status(userId)
        if not bRet:
            return False, sRet

        return True, sRet    

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_sys_status_get)
        if not bRet:
            Log.err("deal_sys_status_get: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)


class ViewDashboardAgents(ViewBase):

    def _deal_agents_get(self):
        bRet, userId = FsmUser.get_user_id(self.get_user_name())
        if not bRet:
            Log.err("username: %s not bussiness" % (self.get_user_name()))
            return bRet, userId

        bRet, sRet = FsmDashboard.det_agents(userId)
        if not bRet:
            return False, sRet

        return True, sRet    

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_agents_get)
        if not bRet:
            Log.err("deal_agents_get: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)


