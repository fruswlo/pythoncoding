# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:42:07 2022

@author: r-ahmed
"""

a0 = int(input("Value of 1st round : "))
a1 = int(input("Value of 2nd round : "))
a2 = int(input("Value of 3rd round : "))
a3 = int(input("Value of 4th round : "))
a4 = int(input("Value of 5th round : "))
a5 = int(input("Value of 6th round : "))
a6 = int(input("Value of 7th round : "))
a7 = int(input("Value of 8th round : "))
a8 = int(input("Value of 9th round : "))
a9 = int(input("Value of 10th round : "))

evenCount = 0
oddCount = 0

if a0 % 2 == 0:
    evenCount = evenCount + 1
else:
    oddCount = oddCount + 1
    
if a1 % 2 == 0:
    evenCount = evenCount + 1
else:
    oddCount = oddCount + 1
    
if a2 % 2 == 0:
    evenCount = evenCount + 1
else:
    oddCount = oddCount + 1
    
if a3 % 2 == 0:
    evenCount = evenCount + 1
else:
    oddCount = oddCount + 1
    
if a4 % 2 == 0:
    evenCount = evenCount + 1
else:
    oddCount = oddCount + 1
    
if a5 % 2 == 0:
    evenCount = evenCount + 1
else:
    oddCount = oddCount + 1
    
if a6 % 2 == 0:
    evenCount = evenCount + 1
else:
    oddCount = oddCount + 1
    
if a7 % 2 == 0:
    evenCount = evenCount + 1
else:
    oddCount = oddCount + 1

if a8 % 2 == 0:
    evenCount = evenCount + 1
else:
    oddCount = oddCount + 1
    
if a9 % 2 == 0:
    evenCount = evenCount + 1
else:
    oddCount = oddCount + 1

print()
print("No of Even digits : ", evenCount)
print("No of Odd digits : ", oddCount)