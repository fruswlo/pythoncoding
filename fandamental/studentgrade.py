# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 01:27:20 2022

@author: r-ahmed
"""


marks = float(input("Enter student marks : "))

if marks >= 80.00 and marks <= 100.00:
    print(marks, "Obtained Grade = A+")
elif marks >= 70.00 and marks <= 79.99:
    print(marks, "Obtained Grade = A")
elif marks >= 60.00 and marks <= 69.99:
    print(marks, "Obtained Grade = A-")
elif marks >= 50.00 and marks <= 59.99:
    print(marks, "Obtained Grade = B")
elif marks >= 40.00 and marks <= 49.99:
    print(marks, "Obtained Grade = C")
elif marks >= 33.00 and marks <= 39.99:
    print(marks, "Obtained Grade = D")
elif marks >= 0 and marks < 33.99:
    print(marks, "Obtained Grade = F")
else:
    print("Invalid marks!")