#binary search
l=[]
flag=0
n=int(input("enter total no of elements\n"))
for i in range(0,n):
    n1=int(input("enter no\n"))
    l.append(n1)
print(l)
############################
#bubble sort
for r in range(0,n):
    for c in range(0,(n-1)-r):
        if l[c]>l[c+1]:
            t=l[c]
            l[c]=l[c+1]
            l[c+1]=t
for i in range(0,n):
    print(l[i],end=' ')
############################
item=int(input("\n enter item\n"))    
###########################        
a=0
b=n-1
m=(a+b)//2
#print("index",m)
#print("mid",l[m])
while flag==0:
    if a>b:
        #print("a",a)
        #print("b",b)
        print("item is not found")
        flag=1
    
    elif item>l[m]:
        a=m+1
        m=(a+b)//2
        #print("a",a)
        #print("b",b)
        print("index ",m)
        print("mid",l[m])

    elif item<l[m]:
        b=m-1
        m=(a+b)//2
        #print("a",a)
        #print("b",b)
        print("index",m)
        print("mid",l[m])

    elif l[m]==item:
        #print("a",a)
        #print("b",b)
        print("searched item is: ",l[m])
        flag=1
    
