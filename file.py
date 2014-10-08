#!/usr/bin/env python
# -*- coding: utf-8 -*-

fname='poem.txt'
fstr='''\
        aaaaaaaaaaaaaaaaaaaaaaaaa
        bbbbbbbbbbbbbbbbbbbbbbbbb
        ccccccccccccccccccccccccc'''

f=file(fname, 'w')
f.write(fstr)
f.close()

f=file(fname, 'r')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print line,
f.close()
