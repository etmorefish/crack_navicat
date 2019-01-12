#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-12 19:50:01
# @Author  : lilei (849078367@qq.com)
# @Link    : https://blog.csdn.net/yyx3214/article/details/79428582 
# @Version : $Id$


#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import re

# 试用时间重置的正则
ps = (
        re.compile(r'\[Software\\\\PremiumSoft\\\\Data\\\\\{[^\}]*\}\\\\Info\].*?\n[^\[]*'),
        re.compile(r'\[Software\\\\Classes\\\\CLSID\\\\\{[^\}]*\}\\\\Info\].*?\n[^\[]*')
    )

# user.reg 的路径
regfile = os.path.join(os.environ['HOME'], '.navicat64', 'user.reg')

# 正则替换
with open(regfile, 'r+') as f:
    regstr = f.read()
    for p in ps:
        regstr = p.sub(lambda m: '', regstr)

    f.seek(0, 0)
    f.truncate()
    f.write(regstr)
！