#Bubble sort
l=[]
print("enter no\n")
for i in range(0,5):
    n=int(input())
    l.append(n)
print(l)
for r in range(0,5):
    for c in range(0,(4-r)):
        if l[c]>l[c+1]:
            t=l[c]
            l[c]=l[c+1]
            l[c+1]=t
for i in range(0,5):
    print(l[i],end=' ')

