#sum of even and odd no
n=int(input("enter no of elements\n"))
l=[]
sum1=0
sum2=0
print("enter elements of list\n")
for x in range(1,n+1):
        a=int(input())
        l.append(a)
        if a%2==0:
            sum1=sum1+a
        if a%2!=0:
            sum2=sum2+a
print("list is: ",l)
print("sum of even no is: ",sum1)        
print("sum of odd no is: ",sum2)
input()
