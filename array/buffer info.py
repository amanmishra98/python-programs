#Bufferinfo return the address of buffer in which our array is stored and
#also return the size of array
from array import *
a=array('i',[1,2,3,3,4])
for i in a:
    print(i)
x=a.buffer_info()    
print(x)
