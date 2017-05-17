# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_Agent管理


from view_base import *

from fsm_agent import *


class ViewAgentList(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        render = web.template.frender("templates/agent-list.html")
        return render()

    def POST(self):
        return self.GET()



class ViewAgentAdd(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        render = web.template.frender("templates/agent-add.html")
        return render()

    def POST(self):
        return self.GET()