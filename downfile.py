#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: downfile.py
Author: scue
Email: scue@vip.qq.com
Github: github.com/scue
Description:
    批量请求下载文件
    下载文件不保存于本地，而是直接抛弃之
    因此，并无硬盘io性能的限制
"""


import httplib
import threading
import time

server="localhost"
port=8001
url="/zero.zip" # 下载文件url
number=100      # 下载线程数
timeout = 60000 # 线程超时设定, 单位ms

headers={ 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Referer': 'http://localhost:8001/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2'}

def connslave(index):
    """请求下载的模拟客户端线程"""
    conn = httplib.HTTPConnection(server,port)
    conn.request("GET", url, headers=headers)
    response = conn.getresponse()
    if response.status == 200:
        print "Get OK, client slave number,", index
        response.read()
    else:
        print "response:", response.status
    conn.close

threads = []

for i in range(1, number+1):
    threads.append(threading.Thread(target=connslave, args=(i,)))

for t in threads:
    t.setDaemon(True)
    t.start()

for t in threads:
    t.join(timeout)

# 更简单方式
# import urllib
# urllib.urlretrieve(downurl, None)
