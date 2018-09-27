def ruler(n):
	j=1
	for i in range(1,n+1):
		if((i%10) ==0):
			print(j),
			j=j+1
		else:
			print(' '),
	print("\n")
	for i in range(1,n+1):
		if((i%10) ==0):
			print 0,
		else:
			print (i%10),
n=int(raw_input("Enter ruler value "))
ruler(n)

	
