

print("enter the no of elements:")
n=int(input())

list=[]

print("enter the elements:")

for i in range(n):

	list.append(input())


min=list[0]
max=list[0]

for i in list:
	if(i<min):
		min=i;

print("Min element:",min)

for i in list:
	if(i>max):
		max=i;


print("Max element:",max)

print(list)

list.insert(0,7)

print(list)

del list[0]

print(list)


key=input("enter the element to be searched:")
if key in list:
	print("Element is found\n")
else:
	print("Element Not found\n")
