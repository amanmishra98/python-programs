#insertion sort by user
print("insertion sort by user\n")
l=[]
n1=int(input("enter total no of elements\n"))
for i in range(0,n1):
    n2=int(input("enter element"))
    l.append(n2)
print(l)    
for i in range(1,n1):
    #print("loop i",i)
    for j in range(i-1,0-1,-1):#range(start,stop,step)
        #print("loop j",j)
        if l[i]<l[j]:
            t=l[i]
            l[i]=l[j]
            l[j]=t
        #print("l",l)
        i=i-1
    #print(l)
print(l)
