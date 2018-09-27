'''
import random

r=random.randint(1,9)
t=0
while True:
	
	in1=input("Guess number from 1 to 9 ")
	t=t+1
	if(r>in1):
		print("Guessed low")
	elif(r==in1):
		print("You have guessed correctly \nTotal attemps taken {}\n".format(t))
		c=raw_input("Do you want to continue(Y/N) ")
		if(c.upper()=='Y'):
			r=random.randint(1,9)
			t=0
		else:
			break
	else:
		print("Guessed high")

'''
'''
import turtle

turtle.backward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(40)

turtle.exitonclick()
'''

'''
import turtle
def draw_box(t,x,y,size,fill_color):
    t.penup() # no drawing!
    t.goto(x,y) # move the pen to a different position
    t.pendown() # resume drawing
    t.fillcolor(fill_color)
    t.begin_fill()  # Shape drawn after this will be filled with this color!
    for i in range(0,4):
        board.forward(size) # move forward
        board.right(90) # turn pen right 90 degrees
    t.end_fill() # Go ahead and fill the rectangle!
 
def draw_chess_board():
    square_color = "black" # first chess board square is black
    start_x = 0 # starting x position of the chess board
    start_y = 0 # starting y position of the chess board
    box_size = 30 # pixel size of each square in the chess board
    for i in range(0,8): # 8x8 chess board
        for j in range(0,8):
            draw_box(board,start_x+j*box_size,start_y+i*box_size,box_size,square_color)
            square_color = 'black' if square_color == 'white' else 'white' # toggle after a column
        square_color = 'black' if square_color == 'white' else 'white' # toggle after a row!
board = turtle.Turtle()
draw_chess_board()
turtle.done()
'''
'''
d={}
ns=input()
l=map(int,raw_input().split())
nc=input()
for i in range(nc):
    in1=map(int,raw_input().split())
    d[in1[0]]=in1[1]
l= sum([d[i] for i in map(int,d.keys()) if(i in l)])
print l
'''
'''
p=0
ns=input()
l=map(int,raw_input().split())
nc=input()
for i in range(nc):
	in1=map(int,raw_input().split())
	if(in1[0] in l):
		l.remove(in1[0])
		p=p+in1[1]
print p
'''

'''
l=[]
l1=[]
in1=map(int,raw_input().split())
for i in range(in1[0]):
	a=raw_input()
	l.append(a)
for i in range(in1[1]):
	a=raw_input()
	l1.append(a)
print(l,l1)
for i in range(len(l1)):
	for j in range(len(l)):
		if(l1[i] not in l):
			print("-1"),
			break
		elif(l1[i]==l[j]):
			print("%d"%(j+1)),
	
	print("")
'''

'''
from collections import OrderedDict,Counter
l=[]
a=input()
for i in range(a):
	rs=raw_input()
	l.append(rs)
d=Counter(l)
print(len(d))
l1=list(OrderedDict.fromkeys(l))
for i in l1:
    print d[i],
'''


'''
def numo(st):
	d={}
	s=set(st)
	for i in s:
		d[i]=st.count(i)
	print d
in1=raw_input("Enter a string:")
numo(in1)
'''

'''
from collections import OrderedDict
def numo1(st):
	d=OrderedDict()
	s=[]
	s1=list(st)
	for i in s1:
		if i not in s:
			s.append(i)
	for i in s:
		d[i]=st.count(i)
	print d
in1=raw_input("Enter a string:")
numo1(in1)
'''		
'''
from itertools import product
a=map(int,raw_input().split())
b=[]
s1=[]
m1=[]
for i in range(a[0]):
    b1 =map(int,raw_input().split())
    b.append(b1)
    c1=b[i][0]
    m1.append((b[i][1:c1+1]))
res=map(lambda x:sum(i*i for i in x)%a[1],product(*m1))
print(max(res))	
'''


'''
from itertools import product

K,M = map(int,raw_input().split())
N = (list(map(int, raw_input().split()))[1:] for _ in range(K))
print N
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print results
print(max(results))
'''
'''
def cp(*ipt):
	print ipt
	i1=[tuple(p) for p in ipt]
	print i1
	tl=[[]]
	for i in i1:
		tl=[x+[y] for x in tl for y in i]
		print tl
	for j in tl:
		yield tuple(j)
for i in cp((5,4),(7,8,9),(5,7,8,9,10)):
	print i	

'''

'''
from collections import namedtuple

a=int()
b,c,d,e=raw_input().split()
mark=namedtuple(mark,b c d e)
for _ in range(5):
	try:
		inp=raw_input()
'''

'''
a,b=map(int,raw_input().split())
c=map(int,raw_input().split())
for i in range(a):
	d=b%a
	print("{}".format(c[d])),
	b=b+1		
'''

'''
f=open('fggn','w')
print("gopi", file=f)
'''
'''
import fileinput
for line in fileinput.input('/home/gopinath/python2/sample'):
	print(line)
print(fileinput.filename())
print(fileinput.lineno())
print(fileinput.isfirstline())
print(fileinput.isstdin())
print(fileinput.nextfile())
fileinput.close()
'''

'''
d={}
s='google'
for i in s:
	c=0
	for j in s:
		if j==i:
			c=c+1
	d[i]=c
print d
'''

'''
#reverse a string
a=int(raw_input('Enter a value:'))
rev=0
while(a>0):
	b=a%10
	a=a/10
	rev=rev*10+b
print rev
'''

'''	
#lambda
print(map(lambda x:x*x,range(1,10)))
'''

'''
#dictionary comprehension

d={i:i*i for i in range(1,11)}
print d
'''

'''
#string compression -python3
a=input()
i=0
while(i<len(a)):
	c=1
	for j in range(i+1,len(a)):
		if(a[i]==a[j]):
			c=c+1
		else:
			break
	print("("+str(c)+","+str(a[i])+")",end=" ")
	i=i+c
'''

'''
a=int(raw_input())
b=raw_input().split()
n=int(raw_input())
for i in b:
	
'''






