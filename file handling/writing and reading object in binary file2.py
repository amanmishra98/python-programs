class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
students_list=[Student("amit",19),Student("rahul",20),Student("romesh",18),Student("ajay",21)]

def saveStudents():
    import pickle
    f1=open("F:\\Py programs\\file handling\\file2.obj",'wb')
    for s in students_list:
        pickle.dump(s,f1) #syntax:- dump(element that is to be read,file object)
    f1.close()
def viewAllStudents():
    import pickle
    f2=open("F:\\Py programs\\file handling\\file2.obj",'rb')
    s_list=[]
    while True:
        try:
            s_list=s_list+[pickle.load(f2)]# to load data from file to read
        except EOFError:                   # syntax:-load(file object)
            break
    return s_list#yield will not be use
    
saveStudents()
list1=viewAllStudents()
for iterator in list1:
    print(iterator.name," ",iterator.age)
    
    
