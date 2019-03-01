#2.WAPS to define a class Employee with instance variable empid,empname,salary.
#define constructor to initialize member variable.define fun to shhow data.
class Employee:
    def __init__(self,empid,empname,salary):
        print(empid,empname,salary)
eid=int(input("enter id\n"))
name=input("enter name\n")
sal=int(input("enter salary\n"))
c1=Employee(eid,name,sal)

