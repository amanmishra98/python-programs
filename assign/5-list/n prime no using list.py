'''#first n prime no
n=int(input("enter no"))
l=[]
sum=0
for x in range(1,n+1)

'''


#print first n prime no using for loop
#l=[]
i=[1]
n = int(input("Enter the number:"))
for k in range (1, (n+1)):
    c=0
    for j in range (2, (i+1)):
        if (i%j==0):
            c = c+1
            #print(c)

    if (c==1):
          print (i)

    i=i+1
