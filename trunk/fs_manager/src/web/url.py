# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web url路由


from viewset.view_det_events import *
from viewset.view_det_top import *
from viewset.view_det_model import *
from viewset.view_det_webshell import *

from viewset.view_lib_danfunc import *
from viewset.view_lib_fuzzhash import *

from viewset.view_index import *
from viewset.view_agent import *
from viewset.view_msg import *
from viewset.view_user import *
from viewset.view_sys import *
from viewset.view_log import *
from viewset.view_login import *

urls = (
    "/", ViewIndex,
    "/index", ViewIndex,
    "/index.html", ViewIndex,
    "/detection-events.html", ViewDetEvents,
    "/detection-top.html", ViewDetTop,
    "/detection-model.html", ViewDetModel,
    "/detection-webshell.html", ViewDetWebshell,
    "/lib-fuzzhash.html", ViewLibFuzzhash,
    "/lib-danfunc.html", ViewLibDanfunc,
    "/agent-list.html", ViewAgentList,
    "/agent-add.html", ViewAgentAdd,
    "/msg-list.html", ViewMsgList,
    "/msg-send.html", ViewMsgSend,
    "/msg-add.html", ViewMsgAdd,
    "/user-list.html", ViewUserList,
    "/user-add.html", ViewUserAdd,
    "/sys-status.html", ViewSysStatus,
    "/sys-log.html", ViewSysLog,
    "/sys-reboot.html", ViewSysReboot,
    "/login.html", ViewLogin,
    "/login", ViewLogin,
    "/logout", ViewLogout,

    "/api/dashboard/charts", ViewDashboardCharts,
    "/api/dashboard/statistics", ViewDashboardStatistics,
    "/api/dashboard/top_charts", ViewDashboardTopsCharts,
    "/api/dashboard/log_charts", ViewDashboardLogCharts,
    "/api/dashboard/top_webshell", ViewDashboardTopsWebshell,
    "/api/dashboard/sys_status", ViewDashboardSysStatus,
    "/api/dashboard/agents", ViewDashboardAgents,

    "/api/det/events/list", ViewDetEventsList,
    "/api/det/top/list", ViewDetTopList,
    "/api/det/webshell/list", ViewDetWebshellList,

    "/api/lib/fuzzhash/list", ViewLibFuzzhashList,
    "/api/lib/danfunc/list", ViewLibDanfuncList,

    #"/api/agent/list", ViewAgentList,
    #"/api/agent/add", ViewAgentAdd,
    
    #"/api/agent/del", ViewAgentDel,
    #"/api/agent/edit/", ViewAgentEdit,
    #"/api/agent/profile", ViewAgentProfile,

    #"/api/msg/list/list", ViewAgentList,
    #"/api/msg/send/list", ViewAgentSendList,
    #"/api/msg/add/mail", ViewAgentAdd,
    #"/api/msg/add/message", ViewAgentDel,
    #"/api/msg/add/dingding", ViewAgentEdit,
    #"/api/msg/profile", ViewAgentProfile,

    "/api/user/list", ViewApiUserList,
    #"/api/user/add", ViewUserAdd,
    #"/api/user/del", ViewUserDel,
    #"/api/user/edit", ViewUserEdit,
    #"/api/user/profile", ViewUserProfile,

    #"/api/sys/log/list", ViewSysLogList,
    #"/api/sys/log/del", ViewSysLogDel,
    #"/api/sys/whitelist", ViewSysWhitelist,
    #"/api/sys/whitelist/view", ViewWhitelistShow,
    #"/api/sys/whitelist/add", ViewWhitelistAdd,
    #"/api/sys/whitelist/edit", ViewWhitelistEdit,
    #"/api/sys/whitelist/del", ViewWhitelistDel,
)
