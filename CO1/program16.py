"""Create a single string separated with space from two strings by swapping the
character at position 1."""

s1=input("enter first string=")
s2=input("enter second string=")

print(s2[0]+s1[1:]+" "+s1[0]+s2[1:])