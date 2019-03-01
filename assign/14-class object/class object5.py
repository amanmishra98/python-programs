#2.WAPS to define a class Employee with instance variable empid,empname,salary.
#define constructor to initialize member variable.define fun to shhow data. 
class Employee:
    def __init__(self):
        empid=int(input("enter emplloyee id\n"))
        empname=input("enter employee name\n")
        salary=int(input("enter employee salary\n"))
        print(empid,empname,salary)
c1=Employee()        
