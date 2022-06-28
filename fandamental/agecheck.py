# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:13:56 2022

@author: r-ahmed
"""

age1 = int(input("Enter A age : "))
age2 = int(input("Enter B age : "))
age3 = int(input("Enter C age : "))
age4 = int(input("Enter D age : "))
age5 = int(input("Enter E age : "))
age6 = int(input("Enter F age : "))

count = 0

if age1 >= 30:
    count = count + 1
if age2 >= 30:
    count = count + 1
if age3 >= 30:
    count = count + 1
if age4 >= 30:
    count = count + 1
if age5 >= 30:
    count = count + 1
if age6 >= 30:
    count = count + 1

print("Number of 30+ person : ", count)