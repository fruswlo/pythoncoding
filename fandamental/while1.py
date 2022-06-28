# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:21:31 2022

@author: r-ahmed
"""

#https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/

i = 1
while i < 11:
    print(i)
    i = i + 1

print()
print()
print()

for i in range(5):
    print()
    for j in range(i + 1):
        j = j + 1
        print(j, end=" ")

print()
print()
print()

tot = 0
for i in range(1,11):
    tot = tot + i
    
print(tot)

print()
print()
print()

num = 2
for i in range(1,11):
    num = i * 2
    print(num)

print()
print()
print("=================================================")

numli = [12, 75, 150, 180, 145, 525, 50, 100]

for i in numli:
    if i >= 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)
        
print("================================================")
print()
print()

no = 75869
sums = 0
cnt = 0

while no != 0:
    x = no % 10 # here is collecting vagsesh
    no = no // 10 # here is collecting vagfol
    print(x)
    sums =sums + x
    cnt = cnt + 1

print(cnt)
print(sums)

print()

for i in range(5):
    print()
    for j in range(5 - i):
        j = j + 1
        print(j, end=" ")

print()
print()
print("=================================================")

print("Q8")
print()

list1 = [10, 20, 30, 40, 50]
length = len(list1)

print(length)
for i in range(length - 1, 0):
    print(list1[i], end = " ")
    print("Printing 0")

print("=================================================")
print()    
print()    

print("Q9")
print()  

for i in range(-10, 0):
    print(i)
    
print()    
print()   
print()

print("Q10")
print()  

for i in range(1, 6):
    print(i)

print("Done!")

print()    
print()   
print()

print("Q11")
print()  



print("=================================================")
print("Q17")
print()  

tot1 = 0
for i in range(5):
#    print()
    for j in range(i + 1):
        tot1 = j * 2
        j = j + 1
        print(tot1, " ")

print()
print(tot1)

print("=================================================")
print()    
print()    

        
print("Q18")    

for i in range(5):
    print()
    for j in range(i + 1):
        j = j + 1
        print("*", end=" ")
for i in range(5):
    print()
    for j in range(5 - i):
        j = j + 1
        print("*", end=" ")     

print()
print("End of the Exercise!")
        