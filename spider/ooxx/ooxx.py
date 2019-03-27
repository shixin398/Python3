#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time        : 2019/3/26 10:29
#  @Author      : Shitao.Li
#  @Email       : shi_xin398@126.com
#  @Site        : 
#  @File        : ooxx.py
#  @Software    : PyCharm
#  @Description : download png from http://jandan.net/ooxx
#                   本例基于有道翻译、图片下载两个例子，新增正则表达式知识点

import urllib.request
import urllib.parse

import os
import re

url = 'http://jandan.net/ooxx'
url_dbmeinv = 'https://www.dbmeinv.com/index.htm?pager_offset='


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/68.0.3440.75 Safari/537.36')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        return html


def save_pic(folder, pic, name):
    pwd = os.getcwd()
    if folder in pwd:
        pass
    else:
        if os.path.exists(folder):
            # os.chdir(folder)
            pass
        else:
            os.mkdir(folder)
        os.chdir(folder)
    with open(name, 'wb') as f:
        f.write(pic)


def find_page_index(html):
    # print(html)
    temp_str = re.search(r'class="current-comment-page".*?(</span>)', html)
    if temp_str:
        index = re.search(r'\[\d*\]', temp_str.group())
        if index:
            len_index = len(index.group())
            page_index = index.group()[1:len_index - 1]
            print(page_index)
            return page_index


def find_pic_url(url):
    html = url_open(url).decode('utf-8')
    # 使用非贪婪匹配，否则无用信息过多
    temp_str = re.findall(r'<img class=(.+?\.jpg)', html)
    print(temp_str)
    pic_list = []
    for each in temp_str:
        temp = re.findall(r'http.+\.jpg', each)
        for item in temp:
            pic_list.append(item)
    print(pic_list)
    return pic_list


def get_pic_name(pic_html):
    name = re.findall(r'\/(\w+\.jpg)', pic_html)
    print(name)
    return name[0]


# home_page = url_open(url).decode('utf-8')
# new_page_index = find_page_index(home_page)
# current_page_url = url + '/page-' + new_page_index + '#comments'
# pic_list = find_pic_url(current_page_url)
page_index = 10
while page_index > 0:
    pic_list = find_pic_url(url_dbmeinv + str(page_index))
    print(page_index)
    for each in pic_list:
        pic = url_open(each)
        name = get_pic_name(each)
        save_pic('ugly', pic, name)
    page_index = page_index - 1
