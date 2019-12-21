class student:

	def __init__(self,name,age,marks):

		self.name=name
		self.age=age
		self.marks=marks

	def getdata(self):

		print("Enter student details\n Enter student name\n")
		self.name=str(input())

		print("Enter the Age\n")
		self.age=int(input())

		print("Enter the marks for 3 subjects:\n")
		for i in range(0,3):
			self.marks.append(int(input()))


  

	def display(self):
		print("Name: ", self.name)
		print("Age: " ,self.age)
		print("Marks of 3 subjetcs:",self.marks)



s=student(" ",0,[])
s.getdata()
s.display()

