#2.WAPS to define a class Employee with instance variable empid,empname,salary.
#define constructor to initialize member variable.define fun to shhow data.
class Employee:
    def __init__(self,empid,empname,salary):
        print(empid,empname,salary)
eid=int(input("enter id\n"))
name=input("enter name\n")
sal=int(input("enter salary\n"))
if sal>=5100:
        print("this is invalid salary")
        print(eid,name)
else:        
    c1=Employee(eid,name,sal)

#this data is personal
