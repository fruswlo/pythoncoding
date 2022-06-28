# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 23:25:34 2022

@author: r-ahmed
"""

a = float(input("Enter price for cow : "))
b = float(input("Enter avg price for goats : "))

goats_original_price = b * 5

if a > goats_original_price:
    print("Mr. Aziz seems a loser. Cow = ", a , "and Goats price = ", goats_original_price)
else:
    print("Mr. Aziz is a winner. Goats price = ", goats_original_price)