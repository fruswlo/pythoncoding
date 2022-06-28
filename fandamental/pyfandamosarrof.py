# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:33:01 2022

@author: r-ahmed
"""

#P1
print("P1")
alist = [20, 30, 40, 50, 60, 70, 80, 90]

for i in alist:
    print(i, end=" ")
print()

print()
print()

#P2
print("P2")
alist1 = [2, 3, 4, 5]

for i in alist1:
    x = i ** 2
    print(f"Square of {i} is : ", x)
print()

print()
print()

#P3
print("P3")
alist1 = [2, 3, 4, 5]

for i in alist1:
    if i % 2 != 0:
        x = i ** 2
        print(f"Square of {i} is : ", x)
print()

print()
print()

#P4
print("P4")
alist2 = [2, 3, 4, 5]
n = 9

alist2.insert(2, n)

print(alist2)
print()

print()
print()

#P5
print("P5")
alist3 = [6, 7, 8, 9]
alist4 = [1, 2, 3, 4]
print("Method 1 :", alist3 + alist4)
alist3.extend(alist4)
print("Method 2 :", alist3)

print()
print()

#P6
print("P6")
alist5 = [2, 3, 4, 5, 7]

print("Items are : ", alist5)
alist5.pop(4)
print("Items after popping : ", alist5)

print()
print()

#P7
print("P7")
alist6 = [2, 3, 4, 5, 6, 7]

print(alist6[5])
l = len(alist6) + 1

for i in alist6:
    if i == l:
        print(i)
        
print("last item: ", alist6)

print()
print()

#P8
print("P8")
alist5 = [2, 3, 4, 5, 7]

print("Items are : ", alist5)
alist5.reverse()
print("Reverse items : ", alist5)

print()
print()

#P9
print("P9")
astr = "I am learning Python"

print(astr[5:])


print()
print()

#P10
print("P10")
alist7 = [2, 5, 4, 5, 7, 5]

for i in alist7:
    if i == 5:
        print("Found", i)
        alist7.remove(i)
    
print("Reaining items : ", alist7)

li = list(map(int, input().split()))
print(li)
