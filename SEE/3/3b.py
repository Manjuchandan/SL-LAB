from collections import Counter
from functools import reduce

def word_count(fname):
	with open(fname) as f:
		return Counter(f.read().split())



d=word_count("test.txt")

print(d)
print(type(d))

list1=list(d.items())

print(list1)

list1.sort(reverse=True , key=lambda x:x[1])

print(list1)

print("Top 10 words with most occurences:\n")

list2=[]

for i in range(10):
	print(list1[i][0])
	list2.append(list1[i][1])

print(list2)

avg=reduce(lambda a,b:a+b,list2)/len(list2)
print("avg is :",avg)

list2=[x*x for x in list2 if x%2!=0]
print(list2)


