def primepartition(m):
    l=[]
    l1=[]
    i=1
    
    for k in range (1, (m+1)):
        c=0
        for j in range (2, (i+1)):
            if (i%j==0):
                c = c+1
        if (c==1):
              l.append(i)
        i=i+1
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            x=l[i]+l[j]
            l1.append(x)
    for i in l1:
        if i==m:
            return True
            break
    else:
        return False
a=primepartition(7)
print(a)
