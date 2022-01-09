# Display future leap years from current year to a final year entered by user.

current = int(input("enter current year:"))
last = int(input("enter final year:"))
for i in range(current, last + 1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        print(i)
    i = i + 1
