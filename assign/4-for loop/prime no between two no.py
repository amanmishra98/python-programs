#print prime no between two no using while and for loop

n1 = int(input("Enter the number:"))
n2 = int(input("Enter the number:"))
k=n1
while k<=n2:
    c=0
   # k=k+1
    for j in range (2,k+1):
        if (k%j==0):
            c = c+1
            #print(c)

    if (c==1):
          print (k)

    k=k+1

