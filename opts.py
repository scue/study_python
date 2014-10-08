#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt,os,sys

try:
    # Short option syntax: "hv:"
    # Long option syntax: "help" or "verbose="
    opts, args = getopt.getopt(sys.argv[1:], "hv:o:", ["help", "output=", "verbose="])

except getopt.GetoptError, err:
    # Print debug info
    print str(err)

def usage():
    '''
    -h\t--help\t\tprint this help docs
    -v\t--verbose\tset verbose value.
    -o\t--output\tsave info to a file
    '''
    print "usage: %s -h -o filename -v value" %sys.argv[0]

for option, argument in opts:
    if option in ("-h", "--help"):
        usage()
        print usage.__doc__
        sys.exit()
    elif option in ("-v", "--verbose"):
        verbose = argument
    elif option in ("-o", "--output"):
        print "output file is %s" %argument
