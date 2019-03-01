#print first n prime no using for loop
l=[]
l1=[]
i=1
n = int(input("Enter the number:"))
for k in range (1, (n+1)):
    c=0
    for j in range (2, (i+1)):
        if (i%j==0):
            c = c+1
            #print(c)

    if (c==1):
          print (i)
          l.append(i)
          #print(l)

    i=i+1
print(l)
for i in range(0,len(l)):
    print(i)
    for j in range(i+1,len(l)):
        x=l[i]+l[j]
        print(x)
        l1.append(x)
        print(l1)
for i in l1:
    if i==n:
        print("p+q is: ",n)
        break
