# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_风险监测_模型可视化


from view_base import *

from fsm_det_model import *


class ViewDetModel(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        render=web.template.frender("templates/detection-model.html")
        return render()

    def POST(self):
        return self.GET()