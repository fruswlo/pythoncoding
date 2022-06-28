# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 01:14:57 2022

@author: r-ahmed
"""

def add(a, b):
    return a + b

def sub(a,b):
    return a - b

def mul(a, b):
    return a * b

def div(a,b):
    return a / b

print("Addition of a + b =       ", add(10, 5))
print("Subtraction of a + b =    ", sub(10, 5))
print("Multiplication of a + b = ", mul(10, 5))
print("Devidation of a / b =     ", div(10, 5))


def myfunc(y):
    print(y)
    print(x)
    
x = 10
myfunc(x) # How x value was printed under func with variable x

def myfunc1(y = 5):
    print(y)
    
x = 11
myfunc1(x)
myfunc1() # which means, function can be called without args

def myfunc2(li):    # this function is calculating list items only
    res = 0
    for i in li:
        res = res + i
    return res

res = myfunc2([1, 2, 3, 4, 5]) # putting function res in main res variable
print(res)

