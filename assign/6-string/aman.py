#remove duplicate element in string
s=input("enter a string\n")
print(s)
a=set(s)
print(a)
print(type(a))
s=str(a)
print(s)
print(type(s))
count=0
for x in s:
    count+=1
    print(x)
print(count)
input()

