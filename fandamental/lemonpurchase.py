# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 00:08:43 2022

@author: r-ahmed

"""

x = int(input("Enter Rohmot's lemon price : "))
y = int(input("Enter Biijoy's lemon price : "))
m = int(input("Enter lemon avg weight in g : "))

lemon_weight_in_kg = m / 1000

weight_of_rohmots_lemon = lemon_weight_in_kg * 4
weight_of_biijoys_lemon = 1

if x > y and weight_of_rohmots_lemon > weight_of_biijoys_lemon:
    print("Better to buy from Rohmot")
else:
    print("Better to buy from Biijoy")
    
print("Weight of rohmots lemon in KG: ", weight_of_rohmots_lemon)