# Create a string from given string where first and last characters exchanged.   [eg: python -> nythop]

str = input("enter a string:")
print("entered string:", str)
print("after:")
print(str[-1] + str[1:-1] + str[0])