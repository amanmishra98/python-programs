n = int(input("Enter the number:"))
for x in range (2,n+1):
    for y in range (2, x):
        if x%y==0:
              break
        if y==x:
              print(x)
        x++      
