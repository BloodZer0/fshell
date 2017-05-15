# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_msg通知


from view_base import *

from fsm_msg import *


class ViewMsgList(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        render=web.template.frender("templates/msg-list.html")
        return render()

    def POST(self):
        return self.GET()



class ViewMsgSend(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        render=web.template.frender("templates/msg-send.html")
        return render()

    def POST(self):
        return self.GET()


class ViewMsgAdd(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        render=web.template.frender("templates/msg-add.html")
        return render()

    def POST(self):
        return self.GET()