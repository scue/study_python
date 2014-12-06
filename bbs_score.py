#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: appstore.py
Author: scue
Email: scue@vip.qq.com
Github: github.com/scue
Description:
    使用Cookies批量点击某论坛评分
"""

import urllib2
import threading
import sys,os,re

url=sys.argv[1]
fromhash=sys.argv[2]
pid=sys.argv[3]
cookies='--hide--'

tid_pattern = '\d\d+'
tid_match=re.findall(tid_pattern, url)
if len(tid_match) != 0:
    tid=tid_match[0]
else:
    sys.exit()

posturl="http://bbs.fakebbs.com/forum.php?mod=misc&action=rate&ratesubmit=yes&infloat=yes&inajax=1"

headers=[
        ( 'Host', 'bbs.fakebbs.com' ),
        ( 'Connection', 'keep-alive' ),
        ( 'Content-Length', '349' ),
        ( 'Cache-Control', 'max-age=0' ),
        ( 'Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' ),
        ( 'Origin', 'http://bbs.fakebbs.com' ),
        ( 'User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36' ),
        ( 'Content-Type', 'application/x-www-form-urlencoded' ),
        ( 'Referer', url ),
        ( 'Accept-Encoding', 'gzip, deflate' ),
        ( 'Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2' ),
        ( 'Cookie', cookies )
       ]

#postdata="formhash=390402b1&tid="+str(tid)+"&pid="+pid+"&referer=http://bbs.fakebbs.com/forum.php?mod=viewthread&tid="+str(tid)+"&page=0#pid"+ pid +"&handlekey=rate&score1=%2B0&score2=%2B3&score3=%2B3&score6=%2B1&reason=GodLike&ratesubmit=true"

postdata="formhash="+fromhash+"&tid="+str(tid)+"&pid="+pid+"&referer=http://bbs.fakebbs.com/forum.php?mod=viewthread&tid="+str(tid)+"&page=0#pid"+ pid +"&handlekey=rate&score1=%2B0&score2=%2B0&score3=%2B0&score6=%2B1&reason=GodLike&ratesubmit=true"

print "postdata:", urllib2.unquote(postdata)

class ClientSlave(threading.Thread):
    """请求下载的类"""
    def __init__(self, url, filename=None):
        super(ClientSlave, self).__init__()
        self.url, self.filename = url, filename

    def run(self):
        """请求下载的模拟客户端线程"""
        opener = urllib2.build_opener()
        opener.addheaders.extend(headers)
        f = opener.open(self.url, postdata)
        if self.filename == None:
            f.read()
        else:
            data = f.read()
            f1 = open(self.filename, "wb+")
            try:
                f1.write(data);
            except Exception, e:
                raise e
            finally:
                f1.close()
        f.close()

if __name__ == '__main__':
    for i in range(0, 100):
        ClientSlave(posturl).start()
        #ClientSlave(posturl, "fakebbs_%d.html" %i).start()
