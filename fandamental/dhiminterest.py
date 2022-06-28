# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 23:33:53 2022

@author: r-ahmed
"""

balance = 100000

from_janani_bank = (balance * 3.5 / 100) / 6
from_urrmi_bank = (balance * 2 / 100) / 4

janani_amount_in_3_years = from_janani_bank * 3
urrmi_amount_in_3_years = from_urrmi_bank * 3

if janani_amount_in_3_years > urrmi_amount_in_3_years:
    print("Mr. Dhiman is quite winner. Interest Amount = ", janani_amount_in_3_years)
else:
    print("Mr. Dhiman is a loser. Interest Amount = ", urrmi_amount_in_3_years)