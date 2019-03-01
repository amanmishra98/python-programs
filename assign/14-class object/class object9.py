#this program is creating.......
class Employee:
    def ename(self):
        l1=[]
        n=int(input("enter total no of employee name\n"))
        for i in range(1,n+1):
            name=input("enter employee name\n")
            l1.append(name)
        l1.sort()
        print(l1)
    def esalary(self):
         l2=[]
         for i in l1:
             sal=int(input("enter employee salary\n"))
             l2.append(sal)
         l2.sort()
         print(l2)     

         
c1=Employee()
c1.ename()
c1.esalary()
