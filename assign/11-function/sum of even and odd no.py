#sum of even and odd no using TSRS
'''fun definition'''
def sum(l=[]):
    sum1=0
    sum2=0
    for i in l:
        if i%2==0:
            sum1=sum1+i
        if i%2!=0:
            sum2=sum2+i   
    return sum1,sum2
#fun call
l1=[]
n=int(input("enter no of elements\n"))
for x in range(1,n+1):
    a=int(input("enter elements in list\n"))
    l1.append(a)
    
x=sum(l1)
print(x)
input()
