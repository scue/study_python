#!/usr/bin/env python
# encoding: utf-8

import os,sys,subprocess,getopt
import xml.dom.minidom
from xml.dom.minidom import Node

# 代理环境
proxy_user=''
proxy_pass=''
proxy_host='123.123.123.123'
proxy_port=12345

# 输入文件
inputfile=''
outputfile='errout.txt'

try:
    # Short option syntax: "hv:"
    # Long option syntax: "help" or "verbose="
    opts, args = getopt.getopt(sys.argv[1:], "h:p:o:i:", \
            ["host=", "port=", "output=", "input=",  "username=", "password="])

except getopt.GetoptError, err:
    # Print debug info
    print str(err)

for option, argument in opts:
    if option in ("-h", "--host"):
        proxy_host = argument
    elif option in ("-p", "--port"):
        proxy_port = int(argument)
    elif option in ("-i", "--input"):
        inputfile = argument
    elif option in ("-o", "--output"):
        outputfile = argument
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
print "<<< proxy environment: %s" %proxy_env_str

# 解析.repo/manifest.xml文件，取出project节点
doc = xml.dom.minidom.parse('.repo/manifest.xml')
projects = doc.getElementsByTagName('project')

github_projects=[]
google_projects=[]
errorsync_projects=[]

# 执行同步函数
def sync_project(project, env=None):
    """
    执行同步命令
    project: 期望同步的Project name
    """
    cmd="repo sync %s" %project
    print '>>>', cmd
    # 执行同步
    process = subprocess.Popen(cmd, shell=True, env=env,\
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 实时读取STDOUT
    out = process.stdout.readline()
    while out:
        print out,
        out = process.stdout.readline()
    err = process.stderr.readline()
    # 实时读取STDERR
    while err:
        print err,
        err = process.stderr.readline()
    # 等待进程结束获得返回值
    process.poll()
    errcode = process.returncode
    # 若有错误追加到错误数组
    if errcode != 0:
        errorsync_projects.append(project)

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

cur_env=os.environ.copy()
cur_env["http_proxy"]=http_proxy
cur_env["https_proxy"]=https_proxy

flag_input=False
if len(inputfile) != 0:
    try:
        infd=open(inputfile)
        flag_input=True
    except Exception, e:
        raise e
    if flag_input:
        for project in infd:
            project=project.strip('\n')
            if project in google_projects:
                sync_project(project, cur_env)
            else:
                sync_project(project)
        infd.close()
else:
    # 同步来自Google的Project
    for project in google_projects:
        sync_project(project, cur_env)

    # 同步来自Github的Project
    for project in github_projects:
        sync_project(project)

# 输出同步出错的Project
if len(errorsync_projects) != 0:
    flag_output=False
    if len(outputfile) != 0:
        try:
            outfd=open(outputfile, "w+")
            flag_output=True
        except Exception, e:
            raise e
    print '>>> 同步出现了错误的Project: '
    for project in errorsync_projects:
        print project
        if flag_output:
            outfd.write("%s\n" %project)
    if flag_output:
        outfd.close()

    print '>>> 请执行命令以重新同步Project: '
    for project in errorsync_projects:
        if project in google_projects:
            sync_cmd="env %s repo sync %s" %(proxy_env_str, project)
        else:
            sync_cmd="repo sync %s" %project
        print sync_cmd
