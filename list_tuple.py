#!/usr/bin/env python
# -*- coding: utf-8 -*-

# list 列表
shoplist = ['apple', 'mango', 'carrot', 'banana']
print 'I have', len(shoplist), 'items to purchase'

for item in shoplist:
    print item,
print '\n'

shoplist.append('rice')
print 'shoplist is: ', shoplist

shoplist.sort()
print 'shoplist sort: ', shoplist

# tuple 元组
zoo=('wolf', 'elephant', 'penguin')
new_zoo=('monkey', 'dolphin', zoo)
print zoo
print new_zoo
print new_zoo[2][2]

age=22
name='swaproot'
print '%s is %d years old.' %(name, age)
print 'Why is %s playing with that python?' %name
print 'End of new_zoo is %s' %new_zoo[2][2]

# dictionary
ab = {
    'swaroop':'a@b.com',
    'Larry':'b@b.com',
    'matsumot':'c@b.com'
    }
print 'swaroop\'s address is %s.' %ab['swaroop']

for name,addr in ab.items():
    print 'Contact %s at %s.' %(name, addr)
print
if ab.has_key('Larry'):
    print "Larry's addr is %s" %ab['Larry']

print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]

print 'Item 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1]
print 'Item start to end is', shoplist[:]
print 'Item none is', shoplist

name='swaroop'
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:]

# 对象与参考
mylist = shoplist # 参考

del shoplist[0]
print 'shoplist\tis\t', shoplist
print 'mylist\t\tis\t', mylist

del mylist[0]
print 'shoplist\tis\t', shoplist
print 'mylist\t\tis\t', mylist

mylist=shoplist[:]  # make a copy by doing a full slice
del mylist[0]
print 'shoplist\tis\t', shoplist
print 'mylist\t\tis\t', mylist

if name.startswith('swa'):
    print 'Yes, the string start with "swa"'

if 'a' in name:
    print 'Yes, it contains the string "a"'

if name.find('war') != -1:
    print 'Yes, it contains the string "war"'

delimiter = '_*_'
print delimiter.join(mylist)
