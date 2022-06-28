# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 18:22:42 2022

@author: r-ahmed
"""

a = input("Enter a char from u/d/l/r: ")

if a == "u":
    print("Your position is in Up")
elif a == "d":
    print("Your position is in Down")
elif a == "l":
    print("Your position is in Left")
elif a == "r":
    print("Your position is in Right")
else:
    print("Unknown position!!")