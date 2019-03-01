#1.define a class with instance variable rollno,name.semister,branch.also define
#a instance member functions for user input data to set values of instance
#variable and dissplay student data
class Student:
	def setData(self):
		roll=int(input("enter roll no\n"))
		name=input("enter student name\n")
		sem=int(input("enter semister\n"))
		branch=input("enter branch\n")
		print(name,roll,sem,branch)
c1=Student()
c1.setData()
