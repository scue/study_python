#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import mymod

if __name__ == '__main__':
    mymod.sayhi()
    print 'Version', mymod.version
    print dir('sys')
