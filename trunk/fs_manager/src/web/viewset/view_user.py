# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_用户管理


from view_base import *
from hps_bu_user import *


class ViewUser(ViewBase):
    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("user not login!")
            return web.seeother("/login")
        return render.user()

    def POST(self):
        return self.GET()


class ViewUserList(ViewBase):
    def _deal_user_list_get(self):
        return HpsBuUser.get_user_list(self.get_user_name())

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_user_list_get)
        if not bRet:
            Log.err("deal_user_list_get: %s" % (str(sRet)))
            return self.make_error(sRet)
        return self.make_response(sRet)
        return self.make_response(sRet)


class ViewUserAdd(ViewBase):
    def __init__(self):
        self._rDict = {
            "user_name": {'n': 'userName', 't': str, 'v': None},
            "passwd": {'n': 'passwd', 't': str, 'v': None},
            "tel": {'n': 'tel', 't': str, 'v': ''},
            "email": {'n': 'email', 't': str, 'v': ''},
            "role": {'n': 'role', 't': int, 'v': 2}
        }

    def _check_param(self):
        if not self.userName: return False, "param(user_name) is None"
        if not self.passwd: return False, "param(passwd) is None"
        if not self.role: return False, "param(role) is None"

        if self.passwd:
            if len(self.passwd) < 5 or len(self.passwd) > 12:
                return False, u"密码必须是由5~12位的字母、数字或其它字符组成"
            salt = "moresec#"
            self.passwd = comput_md5_text(salt + self.passwd)

        if self.email:
            _RE_EMAIL = re.compile(r'^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$')
            if _RE_EMAIL.match(self.email) is None:
                return False, "param(email) is invalid"
        if self.role:
            if self.role < 1 or self.role > 2:
                return False, "param(role) is invalid"

        return True, None

    def _log_info(self):
        self.logType = SysLogType.LOG_ADD_USER
        self.logAttr = [{'key': u'用户名', 'val': self.userName},
                        {'key': u'用户密码', 'val': self.passwd},
                        {'key': u'用户邮箱', 'val': self.email},
                        {'key': u'用户角色', 'val': UserRole.to_desc(self.role)}]

    def _deal_user_add(self):
        return HpsBuUser.add_user(self.get_user_name(), self.userName, self.passwd, self.tel, self.email, self.role)

    def POST(self):
        if not self.check_login():
            return self.make_error("user not login")

        bRet, sRet = self.process(self._deal_user_add)
        if not bRet:
            Log.err("deal_user_add: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(ViewBase.RetMsg.MSG_SUCCESS)


class ViewUserDel(ViewBase):
    def __init__(self):
        self._rDict = {
            "user_name": {'n': 'userName', 't': str, 'v': None}
        }

    def _check_param(self):
        if not self.userName: return False, "param(user_name) is None"

        return True, ''

    def _log_info(self):
        self.logType = SysLogType.LOG_DEL_USER
        self.logAttr = [{'key': u'用户名', 'val': self.userName}]

    def _deal_user_del(self):
        username = self.html_decode(self.userName)
        return HpsBuUser.del_user(self.get_user_name(), username)

    def POST(self):
        if not self.check_login():
            return self.make_error("user not login")

        bRet, sRet = self.process(self._deal_user_del)
        if not bRet:
            Log.err("deal_user_del: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(ViewBase.RetMsg.MSG_SUCCESS)


class ViewUserEdit(ViewBase):
    def __init__(self):
        self._rDict = {
            'email': {'n': 'email', 't': str, 'v': None}
        }

    def _check_param(self):
        if not self.email: return False, "param(email) is None"
        return True, None

    def _deal_user_edit(self):
        data = {'email': self.email}
        return HpsBuUser.edit_user(self.get_user_name(), data)

    def POST(self):
        if not self.check_login():
            return self.make_error("user not login")

        bRet, sRet = self.process(self._deal_user_edit)
        if not bRet:
            Log.err("deal user edit: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(ViewBase.RetMsg.MSG_SUCCESS)


class ViewUserProfile(ViewBase):
    def _deal_user_info_get(self):
        return HpsBuUser.get_user_profile(self.get_user_name())

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")

        bRet, sRet = self.process(self._deal_user_info_get)
        if not bRet:
            Log.err("deal user info get: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)


class ViewUserPasswdChange(ViewBase):
    def __init__(self):
        self._rDict = {
            'old_passwd': {'n': 'oldPasswd', 't': str, 'v': None},
            'new_passwd': {'n': 'newPasswd', 't': str, 'v': None}
        }

    def _check_param(self):
        if not self.oldPasswd: return False, 'param(old passwd) is None'
        if not self.newPasswd: return False, 'param(new passwd) is None'

        if len(self.newPasswd) < 5 or len(self.newPasswd) > 12:
            return False, u"密码必须是由5~12位的字母、数字或其它字符组成"

        self.newPasswd = comput_md5_text('moresec#' + self.newPasswd)
        self.oldPasswd = comput_md5_text('moresec#' + self.oldPasswd)

        return True, None

    def _deal_user_passwd_change(self):
        return HpsBuUser.change_passwd(self.get_user_name(), self.oldPasswd, self.newPasswd)

    def POST(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_user_passwd_change)
        if not bRet:
            return self.make_error(sRet)
        return self.make_response(ViewBase.RetMsg.MSG_SUCCESS)
