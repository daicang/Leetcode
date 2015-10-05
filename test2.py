#!/usr/bin/python

def func1():
    a, b = 1, 2
#    str1 = "hello!"
    func2(a, b)
    print "a:", a, "b:", b

def func2(a, b):
    a = a + 1
    b = b + 1

func1()
