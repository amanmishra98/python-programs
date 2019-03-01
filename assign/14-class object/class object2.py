#1.define a class with instance variable rollno,name.semister,branch.also define
#a instance member functions for user input data to set values of instance
#variable and dissplay student data
class Student:
	def setData(self,roll,name,sem,branch):
		print(name,roll,sem,branch)
c1=Student()
c1.setData(22,"am",2,"cs")
