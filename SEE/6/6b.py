list1=[]
class sent:

	def __init__(self,s):
		self.s=s;

	
	def reverse(self):
		n=0

		for i in self.s:

			if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U':
				n+=1


		r=" ".join(reversed(self.s.split(" ")))
		tup=(n,r)
		list1.append(tup)



for i in range(0,3):
	obj=sent(str(input("Enter string:")))
	obj.reverse()


list1.sort(reverse=True)
print(list1)

for i in range(0,3):
	print(list1[i][1])
