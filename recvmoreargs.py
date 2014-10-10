#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 传递 *
def powersum(first, *others):
    """docstring for powersum"""
    total = 0
    for i in others:
        total += pow(i, first)
    return total

# 传递 **
def recvtupe(**diction):
    """docstring for recvtupe"""
    if diction.get('a') == 'aaaa':
        print "OK, a='aaaa''"
    if diction.get('b') == 'bbbb':
        print "OK, b='bbbb''"
    if diction.get('c') == 'cccc':
        print "OK, c='cccc''"

print powersum(2,3,4,5,6)

dd={'a':'aaaa', 'b':'bbbb', 'c':'cccc'}
recvtupe(a='aaaa', b='bbbb', c='cccc')
