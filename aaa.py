#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

print '输入的实参：'
for i in sys.argv:
    print i
print '\n\nThe PYTHONPATH is', sys.path, '\n'

if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being import from another modle'
