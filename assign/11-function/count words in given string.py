#count words in string using TSRS
def count(s):
    x=s.split(" ")
    count=0
    for i in x:
        count=count+1
    return count

a=input("enter string to count words\n")
b=count(a)
print("words=",b)
input()
