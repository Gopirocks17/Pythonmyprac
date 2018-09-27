class stack:
	def __init__(self):
		self.stack1=[]
	def addi(self,val):
		return self.stack1.append(val)
	def remov(self):
		return self.stack1.pop()
	def printst(self):
		print self.stack1
o1=stack()
o1.addi('gopi')
o1.addi('gopi1')
o1.printst()
o1.remov()	
o1.printst()	
