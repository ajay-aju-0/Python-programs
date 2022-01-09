#From a list of integers, create a list removing even numbers.

mylist=[12,13,20,45,43,23,36]
for i in mylist:
    if(i%2==0):
        mylist.remove(i)
print(mylist)

#method2
# li=[-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
# print(li)
# print([x for x in li if x%2!=0])

