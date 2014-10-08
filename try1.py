#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    s = raw_input('Enter something: ')
except EOFError, e:
    print
    print 'fuck! you have err!!!'
    raise e # 这会导致程序退出并显示错误位置
except:
    print 'Other error occurred'
print 'Done'
