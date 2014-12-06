#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: appstore.py
Author: scue
Email: scue@vip.qq.com
Github: github.com/scue
Description:
    利用Cookies批量下载图标文件，用于专用测试，无其他用途。
"""

import urllib2
import threading
import sys,os

iconurls = [
        "http://123.123.123.123:1000/html/appstore/appfile_20/20141205170910/safe_icon_app_icon.png",
        "http://123.123.123.123:1000/html/appstore/appfile_64/20141204172157/safe_icon_ic_launcher.png",
        "http://123.123.123.123:1000/html/appstore/appfile_46/20141204154415/safe_icon_icon.png"
        ]

class ClientSlave(threading.Thread):
    """请求下载的类"""
    def __init__(self, url, iconname):
        super(ClientSlave, self).__init__()
        self.url, self.iconname = url, iconname

    def run(self):
        """请求下载的模拟客户端线程"""
        opener = urllib2.build_opener()
        opener.addheaders.append(('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'))
        opener.addheaders.append(('Accept-Encoding', 'gzip, deflate, sdch'))
        opener.addheaders.append(('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2'))
        opener.addheaders.append(('Connection', 'keep-alive'))
        opener.addheaders.append(('Cookie', 'PHPSESSID=020eb6abb0f333fe7a02605b6754c8c3; sinfor_session_id=WA201BE3902F2530E0FAD2C95E97C17C; StateAdminPwd=%5B1%5D'))
        opener.addheaders.append(('Host', '123.123.123.123:1000'))
        opener.addheaders.append(('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'))
        f = opener.open(self.url)
        data = f.read()
        f1 = open(self.iconname, "wb+")
        try:
            f1.write(data);
        except Exception, e:
            raise e
        finally:
            f1.close()

for i in range(0, len(iconurls)):
    ClientSlave(iconurls[i], "icon_%d.png" %i).start()
