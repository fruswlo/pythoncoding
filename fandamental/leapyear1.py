# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 21:14:48 2022

@author: r-ahmed
"""

a = int(input("Enter Year : "))


if (a % 100 != 0 and a % 4 == 0) or (a % 100 == 0 and a % 400 == 0):
    print("Year", a, "is leap year")
else:
    print("Year", a, "is not leap year")
    




