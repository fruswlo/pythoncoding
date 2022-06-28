a = input("Enter a Year : ")

a = int(a)
if a % 100 == 0 and a % 400 == 0:
    print("leap year")
elif a % 100 == 0 and a % 400 != 0:
    print("not leap year")
elif a % 4 == 0 or a % 400 == 0:
    print("leap year")
else:
    print("not leap year")