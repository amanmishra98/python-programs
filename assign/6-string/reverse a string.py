#WAPS to reverse a string by user
s=input("enter string\n")
print("string is: ",s)
print("reverse of string is:",end=" ")
for x in s[len(s)-1::-1]:
    print("%s"%x,end="")
input()    
    
