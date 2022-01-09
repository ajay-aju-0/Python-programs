# construct the pattern using nested loop
limit=int(input("enter the limit:"))
for i in range(1,limit+1):
    for j in range(i):
        print("*",end=" ")
    print()

for m in range(limit-1,0,-1):
    for n in range(m):
        print("*",end=" ")
    print()

