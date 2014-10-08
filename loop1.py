#!/usr/bin/env python
# -*- coding: utf-8 -*-

n=23
#=======================================
running=True
while running:
    g=int(raw_input('Enter an integer: '))
    if g==n:
        print '正确'
        running=False
    elif g<n:
        print '你的小了'
    else:
        print '你的大了'
else:
    print '结束'

#=======================================
for i in range(1, 10, 2):
    print i
else:
    print 'over'

#=======================================
while True:
    s = raw_input('Enter something: ')
    if s=='quit':
        break
    print 'Length of string is, ', len(s)

