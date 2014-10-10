#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: clist.py
Author: scue
Email: scue@vip.qq.com
Github: github.com/scue
Description: python comprehension list demo
"""

def complexi(argv):
    return argv*10+64

listone=[2,3,4]
listtwo=[2*i for i in listone if i>2]
print listtwo
listcpx=[complexi(j) for j in listone if j<4]
print listcpx

