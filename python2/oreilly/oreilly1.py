'''
class first:
	def pr(self):
		pass
class second(first):
	t1=12
	t2=30
	def pr(self):
		print second.__name__, second.__bases__

a=second()
a.pr()
a.t1=13     #a.__dict__
print a.__class__.__name__
print a.t1,a.t2
print a.__dict__
'''
'''
#2. static method
class aclass(object):
	def astatic():
		print 'a static method'
	astatic=staticmethod(astatic)
ins1=aclass()
aclass.astatic()
ins1.astatic()
'''

'''
# 3.class methods
class Abase(object):
	def aclassmet(cls):
		print 'a class method for',cls.__name__
	aclassmet=classmethod(aclassmet)
class deriv(Abase):
	pass
b=Abase()
d=deriv()
b.aclassmet()
Abase.aclassmet()
d.aclassmet()
deriv.aclassmet()
'''
'''
# 4.Properties
class rect(object):
	def __init__(self,width,height):
		self.width=width
		self.height=height
	def getArea(self):
		return self.width*self.height
	area=property(getArea,doc='area of the rectangle')
class optimizerect(rect):
	__slots__='width','height'
	
r=rect(4,3)
#r.area=20  # give error can't set attribute
print(r.area)
op=optimizerect(5,6)
op.ker=1
print(op.__dict__)
print(optimizerect.__slots__)
'''
'''
#strings method
import pprint
s="gotoiTgofOritgo"
s1='    '
print(s.capitalize())
print(s.center(20))
print(s.count('go'))#sub,start,end
print('endswith',s.endswith('tg'))#sub,start,end
print('find',s.find('grt'))#sub,start,end.returns lower index.if not found returns -1
print('rfind',s.rfind('go'))#return higher index
print('index',s.index('go',4))#same as find but raise value error if not found
print("alnum",s.isalnum())
print('title',s.istitle())
print('space',s1.isspace())
print('ljust',s.ljust(25))
print('replace',s.replace('go',''))
print('swapcase',s.swapcase())
x=range(30)
print x
pprint.pprint(x)
'''

#regular expressions
import re
m=re.search('^Goi','Gopinath')
if(m):
	print 'm=match found'
else:
	print 'm=No match'
m1=re.match(r'th$','th')
if(m1):
	print 'm1=match found'
else:
	print 'm1=No match'
m3=re.match(r'\Ago','gopi')
print m3
m4=re.search(r'\bgo\b','gop')
print m4
m5=re.match(r'\B','India')
print m5
m6=re.match(r'go\d?','go1234')
print m6
m7=re.match(r'go\D+','goe2')
print m7
m8=re.match(r'go\s','go in')
print m8
m9=re.match(r'go\w+','goa234')
print m9
m10=re.match(r'go\\+',r'go\1234')
print m10
s1="he is going to help and he did it"
rel=re.compile(r'\bhe\b',re.IGNORECASE)
m11=rel.sub('she',s1,0)
print m11
rel=re.compile(r'\bhe\b',re.IGNORECASE)
m11=rel.subn('she',s1,0)
print m11

'''
#global access
a=1
def glacc():
	global a
	a=a+2
def gl2():
	import oreilly1 as oiy
        oiy.a=5
def gl3():
	import sys
	g3=sys.modules['oreilly1']
	g3.a=6
print("before global %d"%a)
glacc()
print("After global %d"%a)
gl2()
print("After second %d"%a)
gl3()
print("After third %d"%a)
print(a)
'''
'''
#closure function
def maker(N):
	def action(X):
		return X**N
	return action
f=maker(2) #f remembers 2
print(f)
print(f(3))
g=maker(3)# g remembers 3
print(g)
print(g(6))
print(f(4))
'''
'''
#default value in loops
def makeaction():
	acts=[]
	for i in range(4):
		acts.append(lambda x,i=i:i**x) # i=i is default value
	return acts		
a1=makeaction()
print(a1)
print(a1[0](2))
print(a1[2](2))
print(a1[1](2))
print(a1[3](3))
'''
'''
#nonlocal in 3.x
def tester(start):
	state=start
	def nested(label):
		nonlocal state
		print(label,state)
		state+=1
	return nested
f=tester(0)
print(f('hi'))
print(f('ski'))
g=tester(0)
print(g('ghi'))
print(f('skii'))
'''
'''
#state with function attributes
def tester(start):
	def nested(label):
		print(label,nested.state)
		nested.state+=1
	nested.state=start
	return nested
f=tester(0)
print(f('hi'))
print(f('ski'))
g=tester(0)
print(g('ghi'))
print(f('skii'))
print(f.state)
'''
'''
#Tkinter 
import sys,Tkinter
Tkinter.Label(text='Welcome').pack()
Tkinter.Button(text='Exit',command=sys.exit).pack()
Tkinter.mainloop()
'''
'''
#tkinter2
import Tkinter
root=Tkinter.Tk()
tv=Tkinter.StringVar()
Tkinter.Label(textvariable=tv).pack()
Tkinter.Entry(textvariable=tv).pack()
tv.set('Welcome')
Tkinter.Button(text='Exit',command=root.quit).pack()
b=Tkinter.Button()
Tkinter.mainloop()
print(tv.get())
'''



