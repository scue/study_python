#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sayHello():
    """docstring for sayHello"""
    print u'欢迎光临！！'

def myMax(a, b):
    if a>b:
        return a
    else:
        return b

def func(a,b=5,c=10):
    print a,b,c

def ret(a,b,c):
    return a+2,b+3,c+5

sayHello()
print '1,2 max is: ', myMax(1,2)

func(3,7)
func(25,c=24)
func(c=50,a=100)
a,b,c=ret(2,3,5)
print a,b,c
print sayHello.__doc__
