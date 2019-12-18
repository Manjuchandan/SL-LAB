from functools import reduce

list1=[1,2,3,4,5,6]

print(list1)

list2=[x*3 for x in list1]

print(list2)

sum1=reduce(lambda a,b:a+b,list1)
sum2=reduce(lambda a,b:a+b,list2)

print("sum of 1st list:",sum1)
print("sum of 2nd list:",sum2)
