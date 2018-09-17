'''
# file filtering
f1=open("test",'r')
c1=f1.readlines()
for i in c1:
	if i.startswith('#'):
		pass
	else:
		print i,
f1.close()
'''

'''
# print n lines in file
i1=input("Enter no of lines to print:")
f1=open("test",'r')
c1=f1.readlines()
c=0
for i in c1:
	c=c+1
	if (c==i1+1):
		break
	else:
		print i,
f1.close()
'''
'''
#find no of lines in file
file1=raw_input("Enter file name:")
f1=open(file1,'r')
c1=f1.readlines()
c=0
for i in c1:
	if not (i.strip()==''):
		c=c+1	
f1.close()
print("No of lines is {}".format(c))
'''

'''
#pause after each line and display lines
file1=raw_input("Enter file name:")
f1=open(file1,'r')
c1=f1.readlines()
c=0
for i in c1:
	c=c+1
	if c==15:
		break
	else:
		print i,
		raw_input("Press a Key to continue")
f1.close()		
'''

'''
#compare files and print first difference
f1=open("test",'r')
f2=open("test1",'r')
c=1
cl=0
co1=f1.read()
co2=f2.read()
for i,j in zip(co1,co2):
	if(i=='\n' and j=='\n'):
		c=c+1
		cl=0
	elif (i==j):
		cl=cl+1
	else:
		print("Difference in line no {0} and column {1}".format(c,cl+1))
		break
f1.close()
f2.close()
'''
