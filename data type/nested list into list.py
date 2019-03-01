#l=["hello",True,3]
#l=[1,2,[3],[4,[5,6]]]
l=[1,2,[3,["hello",True]],[4,[5,6]]]
# output list 
output = [] 
  
# function used for removing nested  
# lists in python.  
def reemovNestings(l): 
    for i in l: 
        if type(i) == list: 
            reemovNestings(i) 
        else: 
            output.append(i) 
  
# Driver code 
print ('The original list: ', l) 
reemovNestings(l) 
print ('The list after removing nesting: ', output) 
