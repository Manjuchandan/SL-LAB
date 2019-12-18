class rectangle:

	def __init__(self,breadth,length):
		self.breadth=breadth
		self.length=length

	def area(self):
		return self.breadth*self.length



	
print("enter the length")
a=int(input())

print("enter the breadth")
b=int(input())

obj=rectangle(a,b)

print("area:",obj.area())

