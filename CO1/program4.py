#  Count the occurrences of each word in a line of text
s = str(input("enter line of text:"))
count = dict()
words = s.split()

for x in words:
  if x in count:
    count[x] += 1
  else:
    count[x] = 1
print(count)