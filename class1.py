#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person:
    population=0

    def __init__(self, name):
        """docstring for __init__"""
        self.name = name
        print '(Initializing %s)' %self.name
        Person.population += 1

    def sayHi(self):
        print "hello, my name is %s" %self.name

    def __del__(self):
        """delete a instance"""
        print "==> del %s says bye." %self.name
        Person.population -= 1
        if Person.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people left.' %Person.population

    def howMany(self):
        """docstring for howMany"""
        if Person.population == 1:
            print 'I am the only person here'
        else:
            print 'We have %d persons here.' %Person.population

swaroop = Person('Swaroop')
p = Person('scue')
swaroop.sayHi()
p.sayHi()
p.howMany()
