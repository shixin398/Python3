#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time        : 2019/3/25 15:48
#  @Author      : Shitao.Li
#  @Email       : shi_xin398@126.com
#  @Site        : 
#  @File        : translator.py
#  @Software    : PyCharm
#  @Description : 实现有道翻译功能
import json
import urllib.request
import urllib.parse

tobe_translate = input('Please input your word:')
# tobe_translate = '你好' #开发时避免每次输入耽误时间
data = {
    'i': tobe_translate,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15534990752679',
    'sign': '8068ceaab29dca41031a3695a052208a',
    'ts': '1553499075267',
    'bv': '22c4e55facde8e7a20b16e256e9fdfa1',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
    'typoResult': 'false'}


# data转换成request需要的数据类型
data = urllib.parse.urlencode(data).encode('utf-8')

# 发送请求
youdaofanyi = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
with urllib.request.urlopen(youdaofanyi, data) as response:
    html = response.read().decode('utf-8')
    #拿到json数据
    tar = json.loads(html)
    #获取到结果字段信息
    # {'type': 'ZH_CN2EN', 'errorCode': 0, 'elapsedTime': 21, 'translateResult': [[{'src': '你好', 'tgt': 'hello'}]]}
    tgt = tar['translateResult'][0][0]['tgt']
    print(tgt)




