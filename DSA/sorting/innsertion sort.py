#insertion sort
print("insertion sort\n")
l=[31,45,11,89,55,19,21,8,40]
for i in range(1,9):
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
