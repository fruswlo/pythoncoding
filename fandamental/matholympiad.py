# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 23:19:41 2022

@author: r-ahmed
"""

a = int(input("Enter your calss 3 ~ 12 : "))

if a >= 3 and a <= 5:
    print("Primary category")
elif a >= 6 and a <= 8:
    print("Junior category")
elif a >= 9 and a <= 10:
    print("Secondary category")
elif a >= 11 and a <= 12:
    print("Higher second category")
else:
    print("Out of category")