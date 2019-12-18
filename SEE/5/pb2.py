list1=[]
list2=[]
list3=[]

def fahrenit(T):
	res=(T*9/5)+32
	print(res)
	tup=(T,res)
	list1.append(tup)

def kelvin(T1):
	res=T1+273.15
	print(res)
	tup=(T1,res)
	list2.append(tup)

def celcius(T2):
	res=(T2-32)*5/9
	print(res)
	tup=(T2,res)
	list3.append(tup)




while(True):
        
	print("press 1:fahrenit 2:kelvin 3:celcius 4: display 1st 5:display 2nd 6:display 3rd ")
	c1=int(input())

	if c1==1:
	  print("enter the temparature")
	  c=float(input())
	  fahrenit(c)
	elif c1==2:
	  print("enter the temparature")
	  c=float(input())
	  kelvin(c)
	elif c1==3:
	  print("enter the temparature")
	  c=float(input())
	  celcius(c)
	elif c1==4:
	  print(list1)
	elif c1==5:
	  print(list2)
	elif c1==6:
	  print(list3)
	else:
	  break
