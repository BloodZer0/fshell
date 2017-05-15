# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_样本库管理_danfunc


from view_base import *

from fsm_lib_danfunc import *


class ViewLibDanfunc(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        render=web.template.frender("templates/lib-danfunc.html")
        return render()

    def POST(self):
        return self.GET()



