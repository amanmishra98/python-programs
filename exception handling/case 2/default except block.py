x=int(input("enter 1st no\n"))
y=int(input("enter 2nd no\n"))
try:
    a=x/y
    print("division is",a)
    
except TypeError:
    print("invalid attempt")
except:
    print("this is default except block")
print("this is last line of code")
input()
