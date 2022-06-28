# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:09:59 2022

@author: r-ahmed
"""

height1 = float(input("Enter person height in M : "))
height2 = float(input("Enter person height in M : "))
height3 = float(input("Enter person height in M : "))
height4 = float(input("Enter person height in M : "))

if height1 > height2 and height1 > height3 and height1 > height4:
    print("Person 1 is taller")
if height2 > height3 and height2 > height1 and height2 > height4:
    print("Person 2 is taller")
if height3 > height4 and height3 > height1 and height3 > height2:
    print("Person 3 is taller")
if height4 > height1 and height4 > height2 and height4 > height3:
    print("Person 4 is taller")