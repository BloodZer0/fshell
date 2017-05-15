# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: fs_manager web展示主函数


import os

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("../base")
sys.path.append("../dao")
sys.path.append("../bean")
sys.path.append("..")
sys.path.append(".")

os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'

import web
from viewset.view_base import *
from url import urls


# 权限校验
'''
def user_check(handler):
    def _login():
        return True if Session.get_val("user_name") is not None else False

    if not _login():
        if not HpsWhiteList.check_whitelist(get_client_ip()):
            Log.info("ip %s is forbiddance" % get_client_ip())
            return web.notfound()

    return handler()
'''

# 启动
app = web.application(urls, globals())
Session.init(app)
#app.add_processor(user_check)

if __name__ == "__main__":
    try:
        Log.info("fs_web work start!")
        app.run()
        Log.info("fs_web work end!")

    except Exception, e:
        Log.err("fs_web work err(%s)" % (str(e)))

else:
    application = app.wsgifunc()
