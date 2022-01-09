#Sort dictionary in ascending and descending order

dict={"Aswin":7,"Vyshnav":21,"Lijas":2,"Binshad":8,"Murshid":12,"Gokul":1,"Vishnu":18,"Nideesh":17,"Niranjan":5}
l1=list(dict.items())
l1.sort()
print("Dictionary in ascending order : ",l1)

l2=list(dict.items())
l2.sort(reverse=True)
print("Dictionary in descending order : ",l2)