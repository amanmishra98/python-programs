#print first n prime no using while and for loop
i=1
k=1
n = int(input("Enter the number:"))
while k<=n:
    c=0
    k=k+1
    for j in range (2, (i+1)):
        if (i%j==0):
            c = c+1
            #print(c)

    if (c==1):
          print (i)

    i=i+1
