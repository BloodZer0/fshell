# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_dashborad


from view_base import *
from hps_bu_user import *




class ViewIndex(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        return render.dashboard()

    def POST(self):
        return self.GET()


