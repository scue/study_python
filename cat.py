#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: cat.py
Author: scue
Email: scue@vip.qq.com
Github: github.com/scue
Description: 模拟Linux/Unix中的cat，但只能用于文本文件
"""


import sys,time,os,getopt

# 函数: usage()
# 作用: 提示用户如何使用此脚本
def usage(exitval=0):
    print "usage: %s [-h] input_file" %sys.argv[0]
    print '''
    -h\t--help\t\tprint this help docs
    input_file\twhat you want to show
    '''
    sys.exit(exitval)

# 函数: readfile()
# 作用: 读取文本文件并print出来
def readfile(filename):
    try:
        f=file(filename)
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            print line,
    except Exception, e:
        print "read file err, please check input file %s" %filename
    finally:
        f.close()

# getopt
# 获取脚本输入的参数
#---------------------------------------
try:
    # Short option syntax: "hv:"
    # Long option syntax: "help" or "verbose="
    opts, args = getopt.getopt(sys.argv[1:], "hv:", ['help', 'verbose'])

except getopt.GetoptError, err:
    # Print debug info
    print str(err)
    usage(1)

for option, argument in opts:
    if option in ("-h", "--help"):
        usage()
    elif option in ("-v", "--verbose"):
        verbose = argument
#---------------------------------------

# 没有文件输入时提示如何使用
if len(args) < 1:
    usage()

# 主要操作的入口
if __name__ == '__main__':
    for filename in args:
        readfile(filename)
