class sent:

	vowelcount=0
	__vowels="AaEeIiOoUu"

	def __init__(self,strings):
		self.strings=strings

	def reverse(self):
		splitstring=self.strings.split(" ")
		splitstring=splitstring[: : -1]
		print("String before reversal",self.strings)
		self.strings=" ".join(splitstring)
		print("string after reversal:",self.strings)

	def countvowels(self):
		for char in self.strings:
			if char in self.__vowels:
				self.vowelcount+=1
		print(self.vowelcount)


sen1=sent("hello am here")
sen2=sent("hi hemanth")
sen3=sent("hi i am in sl lab")


sen1.countvowels()
sen2.countvowels()
sen3.countvowels()


if sen1.vowelcount > sen2.vowelcount:
	
	if sen1.vowelcount<sen3.vowelcount:
		sen3.reverse()
		sen1.reverse()
	else:
		sen1.reverse()
		sen3.reverse()

	sen2.reverse()

else:

	if sen2.vowelcount < sen3.vowelcount:
		sen3.reverse()
		sen1.reverse()

	else:
		sen1.reverse()
		sen3.reverse()

	sen1.reverse()
