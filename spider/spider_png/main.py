#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time        : 2019/3/25 9:38
#  @Author      : Shitao.Li
#  @Email       : shi_xin398@126.com
#  @Site        : 
#  @File        : main.py
#  @Software    : PyCharm
#  @Description : save a png from http://placekitten.com/

import urllib.request

req = urllib.request.Request('http://placekitten.com/200/300')
response = urllib.request.urlopen(req)
cat_jpg = response.read()

with open('cat_200_300.jpg', 'wb') as f:
    f.write(cat_jpg)

# 注意：with as用法优势：
# 基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
# 紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。
# 当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
