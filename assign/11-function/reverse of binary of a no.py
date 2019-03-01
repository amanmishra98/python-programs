#reverse of binary representation of given no using TSRN
def rev(n):
    b=bin(n)
    c=b[2:]
    print(c)
    print(len(c))
    print("reverse is: ",c[-1::-1])

a=eval(input("enter no\n"))
rev(a)

