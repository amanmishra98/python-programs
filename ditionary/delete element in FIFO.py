#deletion in queue
words={}
l=['a','b','c','d']
for x in l:
    print("enter value for ditionary\n")
    words[x]=input()
print(words)
print("\n")
print("delete element FIFO\n")    
for x in l:
    del(words[x])
    print(words)
input()
