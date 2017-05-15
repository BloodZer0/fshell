# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_sys设置


from view_base import *

from fsm_sys import *




class ViewSysStatus(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        render=web.template.frender("templates/sys-status.html")
        return render()

    def POST(self):
        return self.GET()



class ViewSysLog(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        render=web.template.frender("templates/sys-log.html")
        return render()

    def POST(self):
        return self.GET()


class ViewSysReboot(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        render=web.template.frender("templates/sys-reboot.html")
        return render()

    def POST(self):
        return self.GET()