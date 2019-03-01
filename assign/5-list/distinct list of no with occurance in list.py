#find the occurrance of no in list
n=int(input("enter no\n"))
l=[]

for x in range(1,n+1):
    a=int(input())
    l.append(a)
    y=l.count(a)
    if y>1:
        print("occurance of %d is %d: "%(a,y))
input()
