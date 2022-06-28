# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 00:40:24 2022

@author: r-ahmed
"""

a = int(input("Enter 1st no : "))
b = int(input("Enter 2nd no : "))
c = int(input("Enter 3rd no : "))
d = int(input("Enter 4th no : "))
e = int(input("Enter 5th no : "))
f = int(input("Enter 6th no : "))
g = int(input("Enter 7th no : "))

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
if d > largest:
    largest = d
if e > largest:
    largest = e
if f > largest:
    largest = f
if g > largest:
    largest = g
    
lowest = a
if b < lowest:
    lowest = b
if c < lowest:
    lowest = c
if d < lowest:
    lowest = d
if e < lowest:
    lowest = e
if f < lowest:
    lowest = f
if g < lowest:
    lowest = g

larger = a
if b < largest and b > lowest:
    larger = b
if c < largest and c > lowest:
    larger = c
if d < largest and d > lowest:
    larger = d    
if e < largest and e > lowest:
    larger = e
if f < largest and f > lowest:
    larger = f
if g < largest and g > lowest:
    larger = g
    
lower = a
if b < largest and b > lowest:
    larger = b
if c < largest and c > lowest:
    larger = c
if d < largest and d > lowest:
    larger = d    
if e < largest and e > lowest:
    larger = e
if f < largest and f > lowest:
    larger = f
if g < largest and g > lowest:
    larger = g

large = a
if b < larger and b > lower:
    larger = b
if c < larger and c > lower:
    larger = c
if d < larger and d > lower:
    larger = d    
if e < larger and e > lower:
    larger = e
if f < larger and f > lower:
    larger = f
if g < larger and g > lower:
    larger = g

low = a
if b < larger and b > lower:
    larger = b
if c < larger and c > lower:
    larger = c
if d < larger and d > lower:
    larger = d    
if e < larger and e > lower:
    larger = e
if f < larger and f > lower:
    larger = f
if g < larger and g > lower:
    larger = g
    
middle = a
if b < large and b > low:
    larger = b
if c < large and c > low:
    larger = c
if d < large and d > low:
    larger = d    
if e < large and e > low:
    larger = e
if f < large and f > low:
    larger = f
if g < large and g > low:
    larger = g
    
    
if larger > large and lower < low:
    larger = larger
    lower = lower
else:
    larger = large
    lower = low

if large > middle and low < middle:
    large = large
    low = low
else:
    large = middle
    low = middle

if middle <= large and middle >= low:
    middle = middle
else:
    middle = large


    
    
print(lowest, lower, low, middle, large, larger, largest)