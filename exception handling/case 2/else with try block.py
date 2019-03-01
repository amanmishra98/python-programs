x=int(input("enter 1st no\n"))
y=int(input("enter 2nd no\n"))
try:
    a=x/y
    print("division is",a)
except:
    print("this is default except block")
else:
    print("no exception raise in try block so else will run")
print("this is last line of code")
input()
