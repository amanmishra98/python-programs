#knapsack problem
l1=[]
l2=[]
l3=[]
l4=[]
a=0
knapsack=int(input("enter knapsack capacity"))
print("knapsack is: ",knapsack,"kg")
for i in range(0,7):
    l1.append("%.2f"%float(input("enter profit")))
print(l1)
for i in range(0,7):
              l2.append("%.2f"%float(input("enter weight")))
print(l2)
for i in range(0,7):
    x=float(l1[i])/float(l2[i])
    l3.append("%.2f"%x)
print(l3)              
#bubble sort
for r in range(0,7):
    for c in range(0,(7-1)-r):
        if l3[c]<l3[c+1]:
            ##############
            t=l3[c]
            t1=l1[c]
            t2=l2[c]
            ###################
            l3[c]=l3[c+1]
            l1[c]=l1[c+1]
            l2[c]=l2[c+1]
            ###################
            l3[c+1]=t
            l1[c+1]=t1
            l2[c+1]=t2
print("sorted list")
print(l1)
print(l2)
print(l3)
for i in range(0,7):
    if knapsack>eval(l2[i]):
        knapsack=knapsack-eval(l2[i])
        print(knapsack)
        a=a+eval(l1[i])
    else:
        x1=abs((eval(l2[i])-knapsack)-eval(l2[i]))
        print(x1)
        a=a+eval(l3[i])*x1
        break
print(a)
