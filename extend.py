#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 7.py
Author: scue
Email: scue@vip.qq.com
Github: github.com/scue
Description: 简明使用继承的方法
"""


class SchoolMember:
    def __init__(self, name, age):
        """docstring for __init__"""
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s)' % self.name

    def tell(self):
        """docstring for tell"""
        print 'Name: "%s" Age: %s' %(self.name, self.age)

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        """docstring for __init__"""
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialied Teacher: %s)' %self.name

    def tell(self):
        """docstring for tell"""
        SchoolMember.tell(self)
        print 'salary: %d' %self.salary

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        """docstring for __init__"""
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: %s)' %self.name
    def tell(self):
        """docstring for tell"""
        SchoolMember.tell(self)
        print 'marks:', ' '.join(self.marks)

t = Teacher('Mrs. Wang', 24, 8000)
s = Student('Weiqiang Ling', 22, ['aa', 'bb'])

members = [t, s]
for member in members:
    member.tell()
