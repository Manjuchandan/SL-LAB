dict={1:"hydrogen",2:"helium",3:"lithium",4:"berellium"}


def dictionary():

	while True:
		print("enter atomic no\t enter 0 to stop:\n")
		num=int(input())

		if(num==0):
			break


		else:
			print("enter the name of the element\n")
			name=str(input())
			dict.update({num:name})
			print(dict)



	print("No of elements =",len(dict));

	print("enter the element to be serched:\n");
	search=str(input())

	flag=0
	
	for i in dict:
		if(dict[i].lower()==search.lower()):
			print("element found:")
			print({i,dict[i]})
			flag=1
			break;


	if(flag!=1):
		print("element not found:")




dictionary()


