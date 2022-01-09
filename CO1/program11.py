#  Find biggest of 3 numbers entered.

print("enter 3 numbers:")
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print("largest number is :", a)
elif b > a and b > c:
    print("largest number is :", b)
else:
    print("largest number is :", c)