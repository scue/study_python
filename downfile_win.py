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


import sys,os,getopt
import httplib, random

from multiprocessing import Process

DEBUG=False

server="123.123.123.123"
port=443
startnum=1024    # 下载线程数起始
endnum=4096      # 下载线程数结束
twfid="1700009889e91a28"
ids=[1, 2, 3, 4, 5]

# url="/mobileapp/47f00005889e91a2/1.pkg" # 下载文件url, EXAMPLE

headers={ 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Referer': 'https://123.123.123.123/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2'}

def usage(exitval=0):
    print "usage: %s -h host -p port -s startnum -e endnum -t twfid [-d]"\
            %sys.argv[0]
    print '''
    -h\thost
    -p\tport
    -t\ttwfid\t\tDownload TWFID
    -s\tstartnum\tDownload threads number start by
    -e\tendnum\t\tDownload threads number end by
    -d\tdebug\t\tDebug mode, will print more information
    '''
    sys.exit(exitval)

try:
    # Short option syntax: "hv:"
    # Long option syntax: "help" or "verbose="
    opts, args = getopt.getopt(sys.argv[1:], "h:p:s:t:e:d",\
            ["host=", "port=", "number=", "twfid=", "end=", "debug"])

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
    elif option in ("-d", "--debug"):
        DEBUG=True
    elif option in ("-v", "--verbose"):
        verbose = argument
    else:
        print "Unknow option:", option

def clientSlave(index,url):
    """请求下载的模拟客户端线程"""
    conn = httplib.HTTPSConnection(server,port)
    conn.request("GET", url, headers=headers)
    response = conn.getresponse()
    if DEBUG:
        data=response.read()
        filename="down_%d.pkg" %index
        f1=open(filename, "wb+")
        try:
            f1.write(data)
        except Exception, e:
            raise e
        finally:
            f1.close()
    else:
        response.read()
    response.close()
    conn.close

def loop_main(number):
    """后台运行的线程

    :number: TODO
    :returns: TODO

    """
    threads = []
    for i in range(1, number+1):
        rnum=random.choice(ids)
        url="/mobileapp/%s/%d/%d.pkg" %(twfid, rnum, rnum)
        if DEBUG:
            print "Downloading: 'https://%s:%d%s'" %(server, port, url)
        threads.append(Process(target=clientSlave, args=(i,url)))
    for t in threads:
        t.start()
    for t in threads:
        t.join(60000)

if __name__ == '__main__':
    step=256
    for number in range(startnum, endnum+step, step):
        print "Current threads number: ", number
        loop_main(number)
