# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 00:32:21 2022

@author: r-ahmed
"""

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))

if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c

if a < b and a < c:
    smallest = a
if b < a and b < c:
    smallest = b
if c < a and c < b:
    smallest = c

if a < largest and a > smallest:
    middle = a
if b < largest and b > smallest:
    middle = b
if c < largest and c > smallest:
    middle = c
    
print("Smallest -> middle -> Largest : ", smallest, middle, largest)
print("Largest number is : ", largest)
print("Middle number is : ", middle)
