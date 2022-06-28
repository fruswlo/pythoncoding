# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 00:30:34 2022

@author: r-ahmed
"""

number = int(input("Enter a number : "))
cnt = 0

while number != 0:
    cnt = cnt + number % 10
    print(cnt)
    number = number // 10
    print(number)


