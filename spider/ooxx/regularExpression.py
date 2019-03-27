#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time        : 2019/3/26 14:41
#  @Author      : Shitao.Li
#  @Email       : shi_xin398@126.com
#  @Site        : 
#  @File        : regularExpression.py
#  @Software    : PyCharm
#  @Description : regular expression

# 直接字母数字，精确匹配        '00'匹配00
# \d 匹配一个数字             '/d/d'匹配0-9任意两个数字，例如89
# \w 匹配一个字母或数字        '\w\w\d' 可以匹配 'py3' ；
# \s 匹配一个空格
# . 匹配任意字符：数字字母符号   'py.' 可以匹配 'pyc' 、 'pyo' 、 'py!' 等等
# * 表示任意个字符（包括 0 个）
#  + 表示至少一个字符
# ? 表示 0 个或 1 个字符
# {n} 表示 n 个字符
# {n,m} 表示 n-m 个字符

# '\' 转义                    '\-'匹配-

# 更精确匹配
# [] 表示范围，可以和上面内容（. * ?等）连用                  [0-9a-zA-Z\_] 可以匹配一个数字、字母或者下划线
#                             [0-9a-zA-Z\_]+ 可以匹配至少由一个数字、字母或者下划线组成的
#                                   字符串，比如 'a100' ， '0_Z' ， 'Py3000' 等等

# A|B 可以匹配 A 或 B           [P|p]ython 可以匹配 'Python' 或者 'python'

# ^ 表示行的开头                 ^\d 表示必须以数字开头
# $ 表示行的结束                 \d$ 表示必须以数字结束

# Python 的 r 前缀,不进行转义     r'ABC\-001' 是 ABC\-001，若谷没有前缀r，则是ABC-001

# 相关函数 re模块、split函数分割、group分组

import re

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])'
             r':(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])'
             r':(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m, m.group(0), m.group(1), m.group(2), m.group(3))
# 19:05:30 19:05:30 19 05 30


# 练习题，识别email及email中的名字
# 识别email地址：email可能格式<xxx.xxx> xxx.xxx@xxx.xxx，其中<>不是必须部分，'.'也不是必须部分
email_regular = re.compile(r'^(<?\w*\.?\w*\>?\s?)(\w*)(\.?)(\w+)@(\w+)\.(com|cn)$')
# 提取名字, 在1的基础上，提取<>部分即可
email_name = re.compile(r'^(<)(\w+)(\.?)(\w+)(>)')
while 1:
    email_addr = input('输入email地址进行测试：')
    result = email_regular.match(email_addr)
    if result:
        print(result)
        result_name = email_name.match(result.group(1))
        if result_name:
            # 获取长度
            length = len(result_name.group())
            # 拿到<>中的名字
            name = result_name.group()[1:length-1]
            print(name)

# 输入email地址进行测试：<david.zhao> gg.ddd@gmil.com
# <re.Match object; span=(0, 28), match='<david.zhao> gg.ddd@gmil.com'>
# david.zhao
