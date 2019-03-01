#bubble sort by user
print("bubble sort by user")
l=[]
n1=int(input("enter total no of elements\n"))
for i in range(0,n1):
    n=int(input("enter no"))
    l.append(n)
print(l)
for r in range(0,n1):
    for c in range(0,((n1-1)-r)):
        if l[c]>l[c+1]:
            t=l[c]
            l[c]=l[c+1]
            l[c+1]=t
for i in range(0,n1):
    print(l[i],end=' ')

