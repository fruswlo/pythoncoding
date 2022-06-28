# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 21:18:16 2022

@author: r-ahmed
"""

no_of_fishes = int(input("Enter no of fish : "))
amount_of_food = int(input("Enter amount of food : "))

need_food_for_fish = no_of_fishes * 3
need_food_for_a_week = need_food_for_fish * 7

check_amount_of_food = amount_of_food >= need_food_for_a_week
print("Amount of food status : ", check_amount_of_food)