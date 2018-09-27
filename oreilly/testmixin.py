import importlib
def tester(listerclass, sept=False):
	class Super:
		def __init__(self):
			self.data1 = 'spam'
		def ham(self):
			pass
# Superclass __init__
# Create instance attrs
	class Sub(Super, listerclass):
		def __init__(self):
			Super.__init__(self)
			self.data2 = 'eggs'
			self.data3 = 42
		def spam(self): pass # Mix in ham and a __str__
# Listers have access to self
	instance = Sub()
	print(instance)
	if sept: print('-' * 80) # Return instance with lister's __str__
# Run mixed-in __str__ (or via str(x))
# More instance attrs
# Define another method here
def testByNames(modname, classname, sept=False):
	modobject= importlib.import_module(modname) # Import by namestring
	listerclass = getattr(modobject, classname)
# Fetch attr by namestring
	tester(listerclass, sept)
if __name__ == '__main__':
	testByNames('listinstance', 'ListInstance', True)
	testByNames('listinherited', 'ListInherited', True)
	testByNames('listtree','ListTree',False)
