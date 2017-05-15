# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_dashborad


from view_base import *
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
        bRet, sRet = FsmDashboard.det_charts()
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
        bRet, sRet = FsmDashboard.det_statistics()
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
    def GET(self):
        return ''


class ViewDashboardLogs(ViewBase):
    def GET(self):
        return ''


class ViewDashboardTopsWebshell(ViewBase):
    def GET(self):
        return ''


class ViewDashboardSys(ViewBase):
    def GET(self):
        return ''


class ViewDashboardAgents(ViewBase):
    def GET(self):
        return ''


