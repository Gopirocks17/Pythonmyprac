'''
1.
x=10
y=5
print("Addition of x and y is %d"% (x+y))
print("subtraction of x and y is %d"% (x-y))
print("multiplication of x and y is %d"% (x*y))
print("division of x and y is %d"% (x/y))
'''

'''
#2.
a,b,c=23,24,22
if(a>b and a>c):
	print("a is greater")
elif(b>c):
	print("b is greater")
else:
	print("c is greater")
'''


'''
#3.
a=input("Enter a number ")
if(a%2==0):
	print("Number is even")
else:
	print("Number is odd")
'''

'''
#4.prime
a=input("Enter a number to check prime ")
p=[2]
j=3

while(j<=a):
	for i in p:
		if(j%i==0):
			j+=2
			break
	else:
		p.append(j)
		j+=2
print p
if a in p:
	
	print "prime number"
else:
	print "Not prime number"
'''

'''
#5.commandline arguments
#a
import sys

print("First argument %r"%sys.argv[1])	
print("second argument %r"%sys.argv[2])
print("Third argument %r"%sys.argv[3])
print("Fourth argument %r"%sys.argv[4])
print("Fifth argument %r"%sys.argv[5])
'''
'''
#b
import sys

if(sys.argv[1]>sys.argv[2] and sys.argv[1]>sys.argv[3]):
	print(sys.argv[1]+" is greater")
elif(sys.argv[2]>sys.argv[3]):
	print(sys.argv[2]+" is greater")
else:
	print(sys.argv[3]+" is greater")
'''

'''
#6.string operations

str1="Gopinath"
str2=str1[2:5]
print(str1*100)
print(str1+str2)
'''

'''
#7.list operations
l=range(10)
l2=range(5)
for i in l:
	print l
print (l[2:5]) # slicing
print (l*2) #repitition
print (l+l2) #concatenation
'''
'''
#8. tuple operation
l=tuple(range(10))
l2=tuple(range(5))
for i in l:
	print l
print (l[2:5]) # slicing
print (l*2) #repitition
print (l+l2) #concatenation
'''

'''
#12 comparision operator
print("Enter 10 values")
l=[]
lt=[]
ht=[]
av=[]
for i in 'abcdefghij':
	i=input("Enter value ")
	l.append(i)
avg=sum(l)/10
print("Average is: %d"%avg)
for i in l:
	if(i<avg):
		lt.append(i)
	elif(i>avg):
		ht.append(i)
	else:	
		av.append(i)
print("Total number of numbers less than average: %d"%len(lt))
print lt
print("Total number of numbers more than average: %d"%len(ht))
print ht
print("Total number of numbers equal to average: %d"%len(av))
print av
'''

'''
#13 biggest of 4 numbers
import sys
print("Enter 4 different numbers")
a=input("Enter value: ")
b=input("Enter value: ")
c=input("Enter value: ")
d=input("Enter value: ")
if(a>b and a>c and a>d):
	print("%d is greater"%a)
elif(b>c and b>d):
	print("%d is greater"%b)
elif(c>d):
	print("%d is greater"%c)
else:
	print("%d is greater"%d)
'''

'''
#14 
A=[1,2,3,4,5,6,7,8,9,10]
B=['a','b','c','d','e','f','g','h','i','j']
for i in B:
	print i #print all names
in1=input("Index to print ")
print("{0} {1}".format(A[in1-1],B[in1-1]))
for i in A[3:9]:
	print i
for i in A[2:]:
	print i
print A+B
for a,b in zip(A,B):
	print a,b
'''		

'''
#42
n=input("Enter n number")
a=0
b=1
if n==1:
	print a
if n==2:
	print b
if n>2:
	print a,b,
	for _ in range(n-2):
		a,b=b,a+b
		print b,
'''
'''
#43
l=['gopi','India','Madurai','TamilNadu','Apple','Bangalore']

def mysearch(*arg1):
	f=0
	length=len(arg1)
	for i in range(length):
		if arg1[i] in l:
			print("{} is present in the list".format(arg1[i]))
			f=1
			break
		else:
			print("{} is not present in the list".format(arg1[i]))
in1,in2=raw_input("Enter the string to search ").split()
mysearch(in1,in2) 
'''
'''
#44
sum1=lambda x,y:x+y
dif=lambda x,y:x-y
mul=lambda x,y:x*y
div=lambda x,y:x/y
mol=lambda x,y:x%y
flr=lambda x,y:x//y
print(sum1(5,2))
print(dif(5,2))
print(mul(5,2))
print(div(5,2))
print(mol(5,2))
print(flr(5,2))		
'''
'''
#45

def palindrome(stg="malayalam"):
	if (stg==stg[::-1]):
		print("It is a palindrome")
	else:
		print("Not a palindrome")
in1=raw_input("Enter a string")
palindrome(in1)
'''
'''
#46
def bigg(a,b,c,d):
	if(a>b and a>c and a>d):
		print "a is greater"
	elif(b>c and b>d):
		print "b is greater"
	elif(c>d):
		print "c is greater"
	else:
		print "d is greater"
a=input("Enter a ")
b=input("Enter b ")
c=input("Enter c ")
d=input("Enter d ")
bigg(a,b,c,d)
'''
'''
#47
def exte(t,l):
	n=t+tuple(l)
	print n
t=input("Enter t ")
l=input("Enter l ")
exte(t,l)
'''

'''	
#48
#a
def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
def sqr(a):
	return a**(0.5)
def substring(c,d):
	l=c.split(d)
	return l
a=input("Enter a number:")
b=input("Enter a number:")
print("Addition of 2 numbers is {}\n".format(add(a,b)))
print("subtraction of 2 numbers is {}\n".format(sub(a,b)))
print("multiplication of 2 numbers is {}\n".format(mul(a,b)))
print("division of 2 numbers is {}\n".format(div(a,b)))
a1=input("Enter a number for square root:")
print("Square root is {}".format(sqr(a1)))
s1=raw_input("Enter a string with delimeter:")
d1=raw_input("Enter delimeter character to split string to substring")
print("The substring list is {}".format(substring(s1,d1)))
'''
	

#49
f1=open("textsa1","r")
f1.read()
f1.close()
f1=open("new1","w+")
st="this is new file and i am writing in it"
f1.write(st)
f1.close()
f1=open("new1","a")
f1.write("Appending line")
f1.close()









