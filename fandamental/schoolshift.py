# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 18:53:33 2022

@author: r-ahmed
"""

a = input("Enter school name : ")
b = input("Enter shift name : ")

if a == "palasdan" and b == "morning":
    print("You need to wear YELLOW badge")

if a == "palasdan" and b == "afternoon":
    print("You need to wear GREEN badge")

if a == "narendan" and b == "morning":
    print("You need to wear BLUE badge")

if a == "narendan" and b == "afternoon":
    print("You need to wear RED badge")