# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 18:03:34 2022

@author: r-ahmed
"""

a = int(input("Enter birthday of Maliha : "))
b = int(input("Enter birthmonth of Maliha : "))
c = int(input("Enter birthyear of Maliha : "))

d = int(input("Enter birthday of Anindita : "))
e = int(input("Enter birthmonth of Anindita : "))
f = int(input("Enter birthyear of Anindita : "))

if f >= c:
    if e >= b:
        if d >= a:
            print("Maliha is elder than Anindita")
        else:
            print("Anindita is elder than Maliha")
    else:
        print("Anindita is elder than Maliha")
else:
    print("Anindita is elder than Maliha")
