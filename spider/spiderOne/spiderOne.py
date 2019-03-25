#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time        : 2019/3/22 16:58
#  @Author      : Shitao.Li
#  @Email       : shi_xin398@126.com
#  @Site        : 
#  @File        : spiderOne.py
#  @Software    : PyCharm
#  @Description : use urllib function

import urllib.request

with urllib.request.urlopen('https://cn.bing.com/') as f: #加载必应网站
    print(f.read().decode('utf-8')) #读取网址内容，读取的内容为2进制代码，根据网站编码格式，进行解码（utf-8）


