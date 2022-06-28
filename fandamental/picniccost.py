# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 21:31:25 2022

@author: r-ahmed
"""

a = int(input("Enter picnic total fees : "))
b = int(input("Enter picnic spot rent : "))
c = int(input("Others expenditure : "))

spot_expenses = b + c
check_going = spot_expenses < a

print("Possibility of going : ", check_going)