# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-25
# desc: 正则匹配php代码中的函数名


import re

cnt = """
    func_a("pwd");
    func_b($uid);
    func_c('pswd');

    func_d($uid,$uname)
    func_e("uqw",$uwsd);
    func_f()
    func_g("qwe",$uid,"ls",'hehe')
    @fun_l($uid)
"""

reg = re.compile(r"""([a-zA-Z|@]\w+)\(["\w+"|"\w+",|'\w+'|'\w+',|\$\w+|\$\w+,]*\)""")
result = re.findall(reg, cnt)
print result


