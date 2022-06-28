a = int(input("Enter 1st amount : "))
b = int(input("Enter 2nd amount : "))
c = int(input("Enter 3rd amount : "))

x = a + b + c

if x >= 375:
    print("Enjoy Biriyani")
else:
    print("Not sufficient amount")
    
a = int(input())
b = int(input())
c = int(input())

total = a + b + c
is_sufficient_amount = total >= 375

print(is_sufficient_amount)