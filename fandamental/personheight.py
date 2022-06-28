# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 21:58:31 2022

@author: r-ahmed
"""

height1 = float(input("Enter person height in M : "))
height2 = float(input("Enter person height in M : "))

if height1 > height2:
    print("Person 1 is taller")

if height1 < height2:
    print("Person 2 is taller")
    

height1 = float(input("Enter person height in M : "))
height2 = float(input("Enter person height in M : "))
height3 = float(input("Enter person height in M : "))

if height1 > height2 and height1 > height3:
    print("Person 1 is taller")

if height2 > height3 and height2 > height1:
    print("Person 2 is taller")
    
if height3 > height2 and height3 > height1:
    print("Person 3 is taller")