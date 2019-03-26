#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time        : 2019/3/25 17:03
#  @Author      : Shitao.Li
#  @Email       : shi_xin398@126.com
#  @Site        : 
#  @File        : tanslatorTwo.py
#  @Software    : PyCharm
#  @Description : 增加agent及代理，躲避防爬
import json
import random
import urllib.request
import urllib.parse

# tobe_translate = input('Please input your word:')
tobe_translate = '你好'
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
data = urllib.parse.urlencode(data).encode('utf-8')

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

# 增加ip代理
ipList = [
    '110.52.235.75:9999',
    '171.11.179.32:9999',
    '183.146.179.159:9000',
    '112.85.164.150:9999',
    '60.10.22.230:49725'
]
proxyhandler = urllib.request.ProxyHandler({'http': random.choice(ipList)})
opener = urllib.request.build_opener(proxyhandler)
urllib.request.install_opener(opener)


# 使用Request增加user-agent
# 这里注意一点，urlopen和Request是不同的
req = urllib.request.Request(url, data)
print(type(req))
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                             'like Gecko) Chrome/68.0.3440.75 Safari/537.36')
with urllib.request.urlopen(req) as response:
    print(type(response))
    html = response.read().decode('utf-8')
    content = json.loads(html)
    tgt = content['translateResult'][0][0]['tgt']
    print(tgt)

