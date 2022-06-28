# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:15:56 2022

@author: r-ahmed
"""
import math

a = float(input("Enter value for a : "))
b = float(input("Enter value for a : "))

convert_to_cm = b * 2.54

circle_sqr_a = float(math.pi * a ** 2)
circle_sqr_b = float(math.pi * convert_to_cm ** 2)

if circle_sqr_a > circle_sqr_b:
    print("Circle A is bigger than B. Size in CM ", a)
else:
    print("Circle B is bigger than A. Size in CM ", convert_to_cm)