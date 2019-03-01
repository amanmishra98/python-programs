a=float(input("enter value of a\n"))
b=float(input("enter value of b\n"))
c=float(input("enter value of c\n"))
x1=(-b+(b*b-4*a*c))/2*a
x2=(-b-(b*b-4*a*c))/2*a

if b*b-4*a*c>0:
    print(x1)
    print(x2)
    print("roots are real and unequal")
if b*b-4*a*c==0:
    print(x1)
    print(x2)
    print("roots are real and equal")
if b*b-4*a*c<0:
    print(x1)
    print(x2)
    print("roots are unequal and imaginary")
input()
