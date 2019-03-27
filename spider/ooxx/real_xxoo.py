#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time        : 2019/3/27 14:27
#  @Author      : Shitao.Li
#  @Email       : shi_xin398@126.com
#  @Site        : 
#  @File        : real_xxoo.py
#  @Software    : PyCharm
#  @Description :

import urllib.request
import urllib.parse

import os
import re
from base64 import urlsafe_b64decode

url = 'http://jandan.net/ooxx'


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/68.0.3440.75 Safari/537.36')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        return html


def find_page_index(html):
    # print(html)
    temp_str = re.search(r'class="current-comment-page".*?(</span>)', html)
    if temp_str:
        index = re.search(r'\[\d*\]', temp_str.group())
        if index:
            len_index = len(index.group())
            page_index = index.group()[1:len_index - 1]
            print(page_index)
            return int(page_index)


def find_pic_url(url):
    html = url_open(url).decode('utf-8')
    # print(html)

    # 提取当前网页中每张图片的hash
    # 使用非贪婪匹配
    pic_hash = re.findall(r'<span class="img-hash">(.*?=)</span>', html)

    # TODO:拼接图片网址, ooxx工程师挺坑啊，写了一堆代码，其实都是糊弄人的。
    # 网址就是：base64_decode(d)，d就是pic_hash
    pic_list = []
    for each in pic_hash:
        temp = urlsafe_b64decode(each)
        # TODO:decode返回值是bytes格式:<class 'bytes'>
        # b'//ws1.sinaimg.cn/mw600/6e6f0cd7gy1g1h9t4wzbmj218w0u0jxp.jpg'，需要强制转换并切片
        temp_len = len(temp)
        # temp_len得到的长度不包括首字母b'，所以切片时尾部需要+2，头部从2开始
        temp_str = str(temp)[2: temp_len + 2]
        # 拼接成http网址，否则urllib无法访问
        temp_list = 'http:' + temp_str
        # print(temp_list)
        pic_list.append(temp_list)
    # print(pic_list)
    return pic_list


def get_pic_name(pic_url):
    name = re.findall(r'\/(\w+\.jpg)', pic_url)
    print(name)
    return name[0]


# 注意判断文件夹是否存在的情况，及存在不存在切换目录
def save_pic(folder, pic, name):
    pwd = os.getcwd()
    if folder in pwd:
        pass
    else:
        if os.path.exists(folder):
            pass
        else:
            os.mkdir(folder)
        os.chdir(folder)
    with open(name, 'wb') as f:
        f.write(pic)


count = 5
home_page = url_open(url).decode('utf-8')
home_page_index = find_page_index(home_page)
while count > 0:
    new_page_index = str(home_page_index - count + 1)
    current_page_url = url + '/page-' + new_page_index + '#comments'
    pic_list = find_pic_url(current_page_url)
    for each in pic_list:
        name = get_pic_name(each)
        pic = url_open(each)
        save_pic('xxoo', pic, name)
    count = count - 1
