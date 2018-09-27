from inherit import server,pizrobot

class customer:
	def __init__(self,name):
		self.name=name
	def order(self,serve):
		print(self.name,'orders from',serve)
	def pay(self,serve):
		print(self.name,'paid to',serve)


class oven():
	def bake(self):
		print("oven bakes")


class pizzashop():
	def __init__(self):
		self.serve=server('bob')
		self.chef1=pizrobot('pat')
		self.oven1=oven()
	def order(self,name):
		cust1=customer(name)
		cust1.order(self.serve)
		self.chef1.work()
		self.oven1.bake()
		cust1.pay(self.serve)

if __name__=='__main__':
	scene=pizzashop()
	scene.order('homer')
	
	
	 
