a=input("enter 1st string\n")
b=input("enter 2nd string\n")
c=input("enter 3rd string\n")
if a<b and a<c and b<c:
    print(a)
    print(b)
    print(c)
if a<c and a<c and c<b:
    print(a)
    print(c)
    print(b)
if b<a and b<c and a<c:
    print(b)
    print(a)
    print(c)
if b<c and b<a and c<a:
    print(b)
    print(c)
    print(a)
if c<a and c<b and a<b:
    print(c)
    print(a)
    print(b)
if c<b and c<a and b<a:
    print(c)
    print(b)
    print(a)
input()    
