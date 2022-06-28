# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 18:29:00 2022

@author: r-ahmed
"""

#x = 100 # Computer programming 1st round
#y = 200 # Win the math
#z = 150 # Misterious world of programming
x = int(input("Enter Computer Programming Book price : "))
y = int(input("Enter Win the Math Book price : "))
z = int(input("Enter Misterious world od Programing Book price : "))

a = int(input("Enter amount on your hand : "))
count = 0

if a >= x:
    count = count + 1
    print("Purchasing X = Computer Programming 1st round")
else:
    count = count + 0

if a >= x + y:
    count = count + 1
    print("Purchasing Y = Win the Math")
else:
    count = count + 0

if a >= x + y + z:
    count = count + 1
    print("Purchasing Z = Misterious world of programming")
else:
    count = count + 0

print("You can purchase : ", count, "books.")