# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 02:21:17 2022

@author: r-ahmed
"""

#File operation test

open("test.txt", "r")
#what above function doing is: it will read the values of that target file.
#So if we want to print the values, then we need to put that file val into a variable

store = open("test.txt","r")

data = store.read()     #read a whole file
#above read() function can read the data in file, but if we again want to display it
#we need to keep into a variable too. here we used data

print(data)

#i we want to read until target char, then we can add args in read funct

store.read(5)
#result = 1000 . it means including the \n until 5 char(byte by byte), it was readng

# here is the function, which returns the cursor position

store.tell()
#if our cursor is in 10th position,it will return that value

#again if we want to bring the cursor at the initial postion, then use seek() func
store.seek(0)

#there is one more function, that is very useful is readline(), it can be used when 
#we do not sure where to reador until how long. so, this func read a full line by line, 
#until EOF

store.readline()    #read line by line
#1000\n
store.readline()
#200\n
store.readline()
#30\n

#here we can see that new line (\n) presenter is also printed. if we want to 
#avoid it, then simply cast the string into int

data1 = store.readline()
print(int(data1))
#5000 . here \n is skipped

# if there are some unnecessary spaces in a line, if we only want to get that data
#except those spaces, then we use strip() func

data1.strip()

#Trying to read an excel file
excel = open("Book1.xlsx", "r")
data3 = excel.read()
print(data3)

#Error. could not open an excel file
store.close()

#when opening a file by open() func, it is mandatory to close the file also at the end
#but we might have fogotten  to close it. which might return an erro. so to solve such
#problem, we can use With/as keyword or write all file operations within the With indent.

with open("test.txt", "r") as txtfile:
    txtfile.readline()
    txtfile.readline()
    txtfile.readline()
    
# it will automatially close the file, once program ended from With indentation

#now write operation on a file

f = open("b.txt", "w")

f.write("Roman")
f.write("Riim\n")
#if we do not put \n, then it will keep writing in same line

f.write("Ramin\n")
f.close()

#after closing if we again open the file in write mode, it will create as new
#and overwrite all previous. 

#If we want to keep that previous, then we need to open the file in append mode

f1 = open("b.txt", "a")
f1.write("Father\n")
f1.write("Mother\n")

#For more aboout file operation, refer
# https://www.programiz.com/python-programming/file-operation#:~:text=three%20lines%5Cn%27%5D-,Python%20File%20Methods,-There%20are%20various










 