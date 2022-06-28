# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 17:31:49 2022

@author: r-ahmed
"""

water_temp = float(input("Enter water temperature : "))

if water_temp < 0:
    print("Ice (solid) : ", water_temp)
if water_temp >= 0 and water_temp <= 100:
    print("Water is liquid : ", water_temp)
if water_temp >= 100:
    print("Steamed (gas): ", water_temp)