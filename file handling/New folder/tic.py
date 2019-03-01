f=open("F:\\New folder\\am.txt","a")
count=0
f.write("hello\n")

f1=open("F:\\New folder\\am.txt","r")
x=f1.readlines()
print(x)
print(type(x))
y=len(x)
print(y)
print(type(y))
for i in x:
    #print(i)
    count=count+1
print("count",count)    
f1.close()
f.close()
f=open("F:\\New folder\\am.txt","w")
f.write("")
f.close()
