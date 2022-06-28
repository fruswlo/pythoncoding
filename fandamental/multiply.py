a = int(input("Enter a number : "))

multiply_by_3 = a % 3 == 0
multiply_by_5 = a % 5 == 0

by_3 = multiply_by_3 or not multiply_by_5
by_5 = multiply_by_5 or not multiply_by_3
by_both = multiply_by_3 and multiply_by_5

print("Multiple by 3 : ", by_3)
print("Multiple by 5 : ", by_5)
print("Multiple by 3 & 5 : ", by_both)
    