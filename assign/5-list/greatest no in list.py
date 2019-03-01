#greatest no in list
n=int(input("enter no"))
l=[]
for x in range(1,n+1):
    a=int(input())
    l.append(a)
print(l)
l.sort()
print(l)
print(l[n-1:n])
input()
