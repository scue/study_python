#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import getopt

def usage(exitval=0):
    print "usage: %s -h -s dirs -o zipfile" %sys.argv[0]
    print '''
    -h\t--help\t\tprint this help docs
    -s\t--source\tinput backup source directories
    -o\t--output\toutput for backup a zip file
    '''
    sys.exit(exitval)

if len(sys.argv) <= 1:
    usage(1)

try:
    # Short option syntax: "hv:"
    # Long option syntax: "help" or "verbose="
    opts, args = getopt.getopt(sys.argv[1:], "hs:o:", ["help", "source=", "output"])

except getopt.GetoptError, err:
    # Print debug info
    print str(err)

src=[]
target=''

for option, argument in opts:
    if option in ("-h", "--help"):
        usage()
    elif option in ("-s", "--source"):
        src.append(argument)
    elif option in ("-o", "--output"):
        target = argument
    elif option in ("-v", "--verbose"):
        verbose = argument
src += args

# src可以是一个列表
def main(target, src):
    targetdir='/tmp/'
    if len(target)==0:
        today=targetdir+time.strftime('%Y%m%d')
        now=time.strftime('%H%M%S')
        if not os.path.exists(today):
            os.mkdir(today)
            print 'mkdir %s' %(today)
    elif not target.startswith(os.sep):
        target = targetdir + target
    #bakcmd="zip -rq '%s' %s" %(target, ' '.join(src))
    bakcmd="tar zcf '%s' %s" %(target, ' '.join(src))
    print "bakcmd: %s" % bakcmd

    if os.system(bakcmd) == 0:
        print 'done'
    else:
        print 'fail'

if __name__ == '__main__':
    main(target, src)
