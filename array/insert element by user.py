from array import *
a=array('i',[])
n=int(input("enter total no of element in array\n"))
for i in range(1,n+1):
    x=int(input("enter no\n"))
    a.append(x)
for i in a:
    print(i,end="")
