# -*- coding: utf-8 -*-
"""
Created on Sat May 28 10:35:48 2022

@author: r-ahmed
"""

from datetime import date
from datetime import datetime


#Solution 1
class Person:
    def __init__(self, name, dob):
        self.name = name    #self.name = object attribute
        self.dob = dob
        
    def __str__(self):
        return "Name: " + self.name + "  DOB: " + self.dob
        
    def calculate_age(self):
        bdt = self.dob
        # convert string to date object        
        dtobj = datetime.strptime(bdt, '%Y-%m-%d').date()
        cdt = date.today()
        
        diff = cdt - dtobj
        days = diff.days
        mont = days/30
        age = mont / 12

        return int(age)
#        return 50

if __name__ == "__main__":
    p1 = Person("Koji","1920-01-01")
    p2 = Person("Taro","1950-02-02")
    p3 = Person("Mori", "1960-03-03")
    
    print("Person 1 age is : ", p1.calculate_age(), "years old")
    print("Person 2 age is : ", p2.calculate_age(), "years old")
    print("Person 3 age is : ", p3.calculate_age(), "years old")



#Solution 2
def age(birthdate):
    dtobj = datetime.strptime(birthdate, '%Y-%m-%d').date()
    today = date. today()
    age = today.year - dtobj.year - ((today.month, today.day) < (dtobj.month, dtobj.day))
    return age

print(age("1982-01-03"))


#Solution 3

birthdate = input("Enter your birthdate :")
my_date = datetime.strptime(birthdate, "%Y-%m-%d")
b_year = my_date.year
b_month = my_date.month
b_date = my_date.day

print(b_year, b_month, b_date)