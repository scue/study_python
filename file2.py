#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: file2.py
Author: scue
Email: scue@vip.qq.com
Github: github.com/scue
Description: cPickle/Pickle demo
"""

# import .. as .. 可以使用更简短的名称
import cPickle as p

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = file(shoplistfile, 'w')
p.dump(shoplist, f) # dump the object to a file
f.close

del shoplist

# read
f = file(shoplistfile)
storedlist = p.load(f) # load the object form a file
print storedlist
