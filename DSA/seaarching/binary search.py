'''binary search'''
l=[2,5,8,12,16,23,38,56,72,91]
item=91
flag=0
#item=int(input("enter item\n"))
for i in range(0,10):
    if l[i]==item:
        print()

    elif i>=9 :
        print("item not found")
        flag=1        
        
a=0
b=9
m=(a+b)//2

#print("index",m)
#print("mid",l[m])
while flag==0:
    if a>b:
        print("item no found")
    elif item>l[m]:
        a=m+1
        m=(a+b)//2
        print("index ",m)
        print("mid",l[m])

    elif item<l[m]:
        b=m-1
        m=(a+b)//2
        print("index",m)
        print("mid",l[m])

    elif l[m]==item:
        print("searched item is: ",l[m])
        flag=1
    
