# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:00:22 2022

@author: r-ahmed
"""

no_of_animal = int(input("Enter no of animals : "))
no_of_choco = int(input("Enter no of chocolates : "))

out_of_jungle = no_of_choco >= no_of_animal
print("Escape from jungle : ", out_of_jungle)