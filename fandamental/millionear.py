# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:05:13 2022

@author: r-ahmed
"""

m1 = int(input("Enter gross amount : "))
m2 = int(input("Enter gross amount : "))
m3 = int(input("Enter gross amount : "))
m4 = int(input("Enter gross amount : "))
m5 = int(input("Enter gross amount : "))
m6 = int(input("Enter gross amount : "))

million = 1000000
count = 0

if m1 >= million:
    count = count + 1
    
if m2 >= million:
    count = count + 1
    
if m3 >= million:
    count = count + 1
    
if m4 >= million:
    count = count + 1
    
if m5 >= million:
    count = count + 1
    
if m6 >= million:
    count = count + 1

print("Number of millionears : ", count)