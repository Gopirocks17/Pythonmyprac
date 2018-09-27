class node:
	def __init__(self,dval=None):
		self.dval=dval
		self.nextval=None
class headlink:
	def __init__(self):
		self.headval=None

	def traverse(self):
		print('*'*30)
		print('linked list values are:')
		p1=self.headval
		while p1 is not None:
			print p1.dval
			p1=p1.nextval
		print('*'*30)
	def AtBegining(self,dval):
		newnode=node(dval)
		newnode.nextval=self.headval
		self.headval=newnode
	def AtEnd(self,dval):
		newnode=node(dval)
		last=self.headval
		if self.headval==None :
			self.headval=newnode
		else:
			while(last.nextval):
				last=last.nextval
			last.nextval=newnode
	def AtMiddle(self,dval,key):
		newnode=node(key)
		middle=self.headval
		while(middle.dval != dval):
			middle=middle.nextval
		newnode.nextval=middle.nextval
		middle.nextval=newnode
	def removel(self,dval):
		trav=self.headval
		try:
			while(trav.nextval.dval != dval):
				trav=trav.nextval
			tmp=trav.nextval
			trav.nextval=tmp.nextval
			tmp.nextval=None
		except:
			if(self.headval.dval==dval):
				self.headval=self.headval.nextval
			else:
				print('Value not exist')	

l1=headlink()
print '1.Insert\n2.Remove\n3.Display\n4.Exit\n'
a=input('Enter your choice:')
while(a!=4):
	if(a==1):
		print('1.Insert at beginning\n2.Insert at End\n3.Insert at Middle\n')
		a1=input('Enter your choice:')
		if a1==1:
			a2=raw_input('Enter Value of node to insert:')
			l1.AtBegining(a2)
		elif a1==2:
			a2=raw_input('Enter Value of node to insert:')
			l1.AtEnd(a2)
		elif a1==3:
			a2=raw_input('Enter Value after node to insert:')
			a3=raw_input('Enter value to insert:')
			l1.AtMiddle(a2,a3)
	elif(a==2):
		a2=raw_input('Enter Value of node to remove:')
		l1.removel(a2)
	elif(a==3):
		l1.traverse()
	else:
		print 'Enter valid input'
	a=input("\n1.Insert\n2.Remove\n3.Display\n4.Exit\n Enter your choice:")
print 'Exited'
