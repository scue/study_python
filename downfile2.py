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


import urllib
import threading
import getopt
import random
import sys,os

server="123.123.139.93"
port=443
url="/mobileapp/47f00005889e91a2/1.pkg" # 下载文件url
startnum=1024    # 下载线程数
endnum=4096      # 下载线程数
step=256
twfid="47f00005889e91a2"

# 取得ID方法:
ids=[100]

def usage(exitval=0):
    print "usage: %s -h host -p port -u url -s startnum -e endnum -t timeout" %sys.argv[0]
    print '''
    -h\thost
    -p\tport
    -t\ttwfid\t\tDownload TWFID
    -n\tstartnum\tDownload threads number start by
    -n\tendnum\t\tDownload threads number end by
    '''
    sys.exit(exitval)

try:
    # Short option syntax: "hv:"
    # Long option syntax: "help" or "verbose="
    opts, args = getopt.getopt(sys.argv[1:], "h:p:u:s:t:e:",\
            ["host=", "port=", "url=", "start=", "twfid=", "end="])

except getopt.GetoptError, err:
    # Print debug info
    print str(err)
    usage()

for option, argument in opts:
    if option in ("-h", "--host"):
        server=argument
    elif option in ("-p", "--port"):
        port=argument
    elif option in ("-s", "--start"):
        startnum=int(argument)
    elif option in ("-e", "--end"):
        endnum=int(argument)
    elif option in ("-t", "--twfid"):
        twfid=argument
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
        urllib.urlretrieve(self.url, None)

def loop_main(number):
    """启动后台运行线程

    :number: 启动线程数

    """
    threads = []
    for i in range(1, number+1):
        rnum=random.choice(ids)
        url="https://%s:%d/mobileapp/%s/%d/%d.pkg" %(server, port, twfid, rnum, rnum)
        #print "Downloading: 'https://%s:%d%s'" %(server, port, url)
        threads.append(ClientSlave(i, url))
    for t in threads:
        t.start()
    print "Current threads number: ", threading.active_count()
    for t in threads:
        t.join(60000000)

if __name__ == '__main__':
    for number in range(startnum, endnum+step, step):
        loop_main(number)
