#WAPS to find no is the greatest no among 3
a=int(input("enter first no\n"))
b=int(input("enter second no\n"))
c=int(input("enter third no\n"))
if a>b and a>c:
    print("a is %d"%a)
    print("a is greatest")
elif b>a and b>c:
     print("b is %d"%b)
     print("b is greatest")
else:
     print("c is %d"%c)
     print("c is greatest")
input()     
    
