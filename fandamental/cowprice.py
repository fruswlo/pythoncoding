# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 00:27:27 2022

@author: r-ahmed
"""

a = int(input("Enter Alam's cow price : "))
b = int(input("Enter Karim's cow price : "))

alom_cow_price = a * 3
karm_cow_price = b * 3

if alom_cow_price > karm_cow_price:
    print("Alom's cow price is higher than Karim")
else:
    print("Karim's cow price is higher than Alom")