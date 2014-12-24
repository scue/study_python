#!/usr/bin/env python
# encoding: utf-8
"""
File: sync_split2.py
Author: scue
Email: scue@vip.qq.com
Github: github.com/scue
Description:
    此脚本主要解决CyanogenMod源码同步时，区分从Github和Google下载的Projects；
    默认情况下大陆可以直接访问Github，而Google则通常需要穿越城墙才能访问得到；
使用方法：
    python sync_split2.py -h proxy_host -p proxy_port
    之后会提示你怎么使用Shell命令行同步，同步Google相关的Project需要准备好Proxy
    Enjoy! (´・ω・｀)
"""


import os,sys,getopt
import xml.dom.minidom
from xml.dom.minidom import Node

# 代理环境
proxy_user=''
proxy_pass=''
proxy_host='123.123.123.123'
proxy_port=12345

f_aosp="aosp.list"
f_github="github.list"

try:
    # Short option syntax: "hv:"
    # Long option syntax: "help" or "verbose="
    opts, args = getopt.getopt(sys.argv[1:], "h:p:", \
            ["host=", "port=", "username=", "password="])

except getopt.GetoptError, err:
    # Print debug info
    print str(err)

for option, argument in opts:
    if option in ("-h", "--host"):
        proxy_host = argument
    elif option in ("-p", "--port"):
        proxy_port = int(argument)
    elif option in ("--username"):
        proxy_user = argument
    elif option in ("--password"):
        proxy_pass = argument
    else:
        print 'unknow argument'

if len(proxy_user) == 0:
    http_proxy="http://%s:%d" %(proxy_host, proxy_port)
    https_proxy="http://%s:%d" %(proxy_host, proxy_port)
else:
    http_proxy="http://%s:%s@%s:%d" %(proxy_user, proxy_pass, proxy_host, proxy_port)
    https_proxy="http://%s:%s@%s:%d" %(proxy_user, proxy_pass, proxy_host, proxy_port)

proxy_env_str="http_proxy=%s https_proxy=%s" %(http_proxy, https_proxy)

# 解析.repo/manifest.xml文件，取出project节点
doc = xml.dom.minidom.parse('.repo/manifest.xml')
projects = doc.getElementsByTagName('project')

github_projects=[]
google_projects=[]

# 对project进行分类
# AOSP的Project保存在 google_projects 数组
# CyanogenMod的Project保存在 github_project 数组
for node in projects:
    remote=node.getAttribute('remote')
    project=node.getAttribute('name')
    groups=node.getAttribute('groups')
    path=node.getAttribute('path')
    if remote == 'aosp':
        if not 'notdefault' in groups:
            google_projects.append(project)
    else:
        github_projects.append(project)

# AOSP
f1=open(f_aosp, "w")
try:
    f1.write(" ".join(google_projects))
except Exception, e:
    raise e
finally:
    f1.close()

# Github
f2=open(f_github, "w")
try:
    f2.write(" ".join(github_projects))
except Exception, e:
    raise e
finally:
    f2.close()

# 提示如何执行脚本
print "repo sync -j4 $(cat %s)" % f_github
print "env %s repo sync -j4 $(cat %s)" % ( proxy_env_str, f_aosp )
