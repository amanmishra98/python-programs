#LCM(lowest common multiple) using TSRS
def lcm(a,b):
    for i in range(2,11):
        x=a*i
        y=b*i
        if x%b==0:
            return(x)
            break   
c=int(input("enter 1st no\n"))
d=int(input("enter 2nd no\n"))
print(c,"\t",d)
y=lcm(c,d)
print("LCM of %d and %d is: %d"%(c,d,y))
input()

