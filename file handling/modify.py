f=open("F:\\Py programs\\file handling\\file1.txt",'r+')
x="agra\n"
s=f.readline()
l=0
while True:
    l=len(s)+l
    if s==x:
        f.seek(l-len(s)+1,0)
        f.write("\nAGRA")
        break
    s=f.readline()
f.close()        
