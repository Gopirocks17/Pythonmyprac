'''
class dad(object):
	def colour(self):
		print("I am brown")
	def charac(self):
		print("I am tough")
class mom(object):
	def colour(self):
		print("I am white")
	def charac(self):
		print("I am cool")
class son(dad,mom):
	def __init__(self):
		print("I am son")
	def colour(self):
		dad().colour()
	def charac(self):
		mom().charac()

s1=son()
s1.colour()
s1.charac()
'''


#Inheritance
class Employee:
	def __init__(self,name,salary=0):
		self.name=name
		self.salary=salary
	def giveraise(self,percent):
		self.salary=self.salary+(self.salary * percent)
	def work(self):
		print(self.name,"does stuff")
	def __repr__(self):
		return("<Name:%s and salary:%d>"%(self.name,self.salary))
class chef(Employee):
	def __init__(self,name):
		Employee.__init__(self,name,50000)
	def work(self):
		print(self.name,"cooks")
class server(Employee):
	def __init__(self,name):
		Employee.__init__(self,name,40000)
	def work(self):
		print(self.name,"serves")
class pizrobot(chef):
	def __init__(self,name):
		chef.__init__(self,name)
	def work(self):
		print(self.name,"makes pizza")
if __name__=='__main__':
	bob=pizrobot('bob')
	bob.giveraise(0.20)
	bob.work()
	print(bob)
	print()
	for clname in Employee,chef,server,pizrobot:
		obj=clname(clname.__name__)
		obj.work()

