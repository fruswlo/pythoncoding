# -*- coding: utf-8 -*-
"""
Created on Fri May 27 21:36:33 2022

@author: r-ahmed
"""

##################################
#Class 03
##################################

from datetime import date
from datetime import datetime


class Person:                           # a python calss
    def __init__(self, name, dob):      # a class constructor method
#        print("Hello")
        # in a calss, when we create an object of that calss, if there is a 
        # constructor method implemented, then it will be called while calling in 
        self.name = name    #self.name = object attribute
        self.dob = dob
        # here "slef.name" and function param "name" is not the same thing. 
        # here self.name or self.dob is a property of the calss Person, where 
        # we are setting that property by the "name" param (by passing) of init
        
        # by this "self" of init method, ref of the obj is passing. using of 
        # self, all ref of objects of the class will be passed correctly 
        
    def __gt__(self, p):                # implement a magic method under class
        # this method is simply to set class attribute to compare between two
        # objects
        return self.dob > p.dob
        
    def __str__(self):      # this type of method called magic method, starts with __
#        return self.name
        # if we implement, __str__ menthod in a class, then output will be as
        # it is defined here. we can also print like below
        return "Name: " + self.name + "  DOB: " + self.dob
        # by implementing this method, a user readable output can be seen
        
    def calculate_age(self):            # implementing a custom method
        bdt = self.dob
#        print(bdt)
        cdt = date.today()
#        print(cdt)
        
        # converting person's date string into datetime object
        dtobj = datetime.strptime(bdt, '%Y-%m-%d').date()
#        print(type(dtobj))
#        print(dtobj)
        
        # getting differences of dates in days
        diff = cdt - dtobj
#        print(diff)
        days = diff.days
#        print(days)
        mont = days/30
#        print(mont)
        age = mont / 12
#        print(int(age))

#        print("Person age is : ", int(age), " years old")
                
        # convert string to date object
        return int(age)

#        return 50

class Car:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
        # this is another class within the same file (in python its possible).
        # here we also initialized self.name, self.year attribute of class Car


        # when we use "self" in function param, which helps to intract with the
        # class object to pass the ref. if we do not use self in a method
        # then eithwe we have to directly call the function with Class name
        # ex: Person.calculate_age()
        # but when we are using class obj to call the function, we must put 
        # self as param

if __name__ == "__main__":
    p1 = Person("Roman","1982-01-03")
#    print(p1.name)
#    print(p1.dob)
    print(p1)       # we can call by this object, because we created __str__
    p2 = Person("Ramin","1993-05-11")
    p3 = Person("Rimaa", "2017-02-12")
#    print(p2.name)
#    print(p2.dob)
    print(p2)
    print(p3)
    
    print(p1 > p2)      # here p1 and p2 both are objects of same calss Person
                        # and we implemented a __gt__ (greatter than) check 
                        # magic method to compare between two objects
    
    c1 = Car("Toyota", "2000")
    print(p1 > c1)      # but here that comparison is not possible, because they 
                        # are fro different calss as well as Car class does not 
                        # have implemented a __gt__ method, so error
    
    
    
    print("Person 1 age is : ", p1.calculate_age(), "years old")
    print("Person 2 age is : ", p2.calculate_age(), "years old")
    print("Person 3 age is : ", p3.calculate_age(), "years old")
    
    #Even the calss name is Same but each class obejct return different, means
    #they are not same
#    print(p1 == p2)     # this will return false, because of that
