def isListOfInts(l2):	
	k=0		
	if((len(l2))==0):
		k=1
	else:
		for i in l2:
			if (type(i) is int):
				k=1
			else:
				k=0
				break
					
	return(k==1)
l2=input("List as input ")
if(not (type(l2) is list)):
	print "arg not of<list> type"
else:
	b=isListOfInts(l2)
	print b		
					
