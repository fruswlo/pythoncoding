# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 23:51:28 2022

@author: r-ahmed
"""

a = int(input("Enter amount on hand : "))
b = bool(int(input("Enter pickle man's availability 0/1 : ")))

if a > 10 and b == False:
    print("Raihan will get an Icecream")
elif a > 10 and b == True:
    print("Raihan will go for pickles")
else:
    print("Raihan does not have enough money !")
