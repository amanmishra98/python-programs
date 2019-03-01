#n prime no using TSRN
def prime(n):
    i=1
    k=1
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
a=int(input("Enter the number:"))
prime(a)    
