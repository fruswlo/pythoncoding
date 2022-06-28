# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:05:13 2022

@author: r-ahmed
"""

bus_total_seats = int(input("Enter no of seats : "))
current_passengers = int(input("Enter passengers no : "))

possibility_to_ride = current_passengers + 5 <= bus_total_seats
print("Possibility of riding bus : ", possibility_to_ride)