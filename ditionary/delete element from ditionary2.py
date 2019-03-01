#deletion in stack
words={}
l=['a','b','c','d']
for x in l:
    print("enter value for ditionary\n")
    words[x]=input()
print(words)
print("\n")
print("delete element LIFO\n")
for x in l[-1::-1]:
    del(words[x])
    print(words)
input()
