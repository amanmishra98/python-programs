x=int(input("enter 1st no\n"))
y=int(input("enter 2nd no\n"))
z=input("enter 3rd no\n")
try:
    a=x/y
    print("division is",a)
    b=x+z
    print("sum is:",b)
except (ZeroDivisionError,TypeError):
    print("invalid attempt")
print("this is last line of code")
input()
