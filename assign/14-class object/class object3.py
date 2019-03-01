#1.define a class with instance variable rollno,name.semister,branch.also define
#a instance member functions for user input data to set values of instance
#variable and dissplay student data
class Student:
	def setData(self,name,roll,sem,branch):
		print(name,roll,sem,branch)
c1=Student()
n=input("enter student name\n")
r=int(input("enter student roll\n"))
s=int(input("enter semister\n"))
b=input("enter branch\n")
c1.setData(n,r,s,b)
