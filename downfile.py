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
import getopt
import sys,os

server="200.200.139.93"
port=443
url="/mobileapp/47f00005889e91a2/1.pkg" # 下载文件url
number=2      # 下载线程数
timeout = 60000 # 线程超时设定, 单位ms


headers={ 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Referer': 'http://localhost:8001/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2'}

def usage(exitval=0):
    print "usage: %s -h host -p port -u url -n number -t timeout" %sys.argv[0]
    print '''
    -h\thost
    -p\tport
    -u\turl\t\tDownload Url, start with "/"
    -n\tnumber\tDownload threads number
    -t\ttimeout\tDownload thread timeout setting
    '''
    sys.exit(exitval)

try:
    # Short option syntax: "hv:"
    # Long option syntax: "help" or "verbose="
    opts, args = getopt.getopt(sys.argv[1:], "h:p:u:n:t:",\
            ["host=", "port=", "url=", "number=", "timeout="])

except getopt.GetoptError, err:
    # Print debug info
    print str(err)
    usage()

for option, argument in opts:
    if option in ("-h", "--host"):
        server=argument
    elif option in ("-p", "--port"):
        port=argument
    elif option in ("-u", "--url"):
        url=argument
    elif option in ("-n", "--number"):
        number=int(argument)
    elif option in ("-t", "--timeout"):
        timeout=argument
    elif option in ("-v", "--verbose"):
        verbose = argument
    else:
        print "Unknow option:", option

class ClientSlave(threading.Thread):
    """请求下载的类"""
    def __init__(self, index, url):
        super(ClientSlave, self).__init__()
        self.index, self.url = index, url

    def run(self):
        """请求下载的模拟客户端线程"""
        conn = httplib.HTTPSConnection(server,port)
        conn.request("GET", self.url, headers=headers)
        response = conn.getresponse()
        lock = threading.Lock()
        if response.status == 200:
            lock.acquire()
            try:
                print "Get OK, client slave number %d" %self.index
                sys.stdout.flush()
            except Exception, e:
                raise e
            finally:
                lock.release()
            response.read()
        else:
            print "response:", response.status
        conn.close

if __name__ == '__main__':
    threads = []
    for i in range(1, number+1):
        threads.append(ClientSlave(i, url))
    for t in threads:
        t.start()

# 更简单方式
# import urllib
# urllib.urlretrieve(downurl, None)
