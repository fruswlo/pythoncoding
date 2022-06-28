# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 21:49:23 2022

@author: r-ahmed
"""

a = float(input("Enter hills size in CM : "))
b = float(input("Enter muntain size in CM : "))
c = float(input("Enter tila size in CM : "))
shoe_size = float(input("Enter shoes size in CM : "))

if a == shoe_size:
    print("Shoes will be given to Hills")
elif b == shoe_size:
    print("Shoes will be given to Mountain")
elif c == shoe_size:
    print("Shoes will be given to Tila")
else:
    print("Shoes for online SALE")