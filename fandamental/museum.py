# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 17:43:21 2022

@author: r-ahmed
"""

ticket_price = int(input("Enter ticket price : "))
money_on_hand = int(input("Enter your momey on hand : "))

purchase_possibility = not (ticket_price > money_on_hand)

print("Your possibility to enter museum : ", purchase_possibility)