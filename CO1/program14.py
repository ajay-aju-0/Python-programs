#Accept an integer n and compute n+nn+nnn.

n=int(input("enter a number,n="))
nn=n*10+n
nnn=n*100+nn
print("n+nn+nnn=",n+nn+nnn)