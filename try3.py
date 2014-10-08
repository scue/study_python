#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: try3.py
Author: scue
Email: scue@vip.qq.com
Github: github.com/scue
Description: try .. finally ..
"""
import time

fname='poem.txt'

try:
    f = file(fname)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()
    print 'Cleaning up.. close the file'
