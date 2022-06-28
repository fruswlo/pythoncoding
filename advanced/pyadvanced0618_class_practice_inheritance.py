# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 21:52:49 2022

@author: r-ahmed
"""

class Vehicle:
    
    # Constructor function. This is called when creating a class object (v1)
    def __init__(self, make, typ):
        self.make = make
        self.typ = typ
        
    
    #This function is retuning the type of object it gets. Using constructor 
    #method __init__, class properties are passed to it objects
#    def get_type(self):
#        return self.typ
    
    def turn_left(self, degree=0):
        print("Turning left", degree, "degree")
        
    def change_gear(self, gear):
        self.gear = gear

class Car(Vehicle):
    
    def turn_left(self, degree=0):
        print("Turning left")
        
        
if __name__ == "__main__":
    v1 = Vehicle("Toyota","Car")
#    v2 = Vehicle("Suzuki","Motorbike")
    v2 = Car("Kawasaki", "Motorbike")
    
        
#    print(v1.get_type()) 
#    print(v2.get_type())
    print(v2.make, v2.typ)
    print(v1.turn_left())   # it will call function from Base class Vehicle
    print(v2.turn_left())   # it will call fnction from subclass Car