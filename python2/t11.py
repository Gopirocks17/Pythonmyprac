'''def mymap(func,*seq):
	res=[]
	for args,argt in zip(*seq):
		print args,argt
		yield func(args,argt)
print(list(mymap(pow,[1,2,3],[4,3,2])))
'''
def myzip(*args):
	iters = map(iter, args)
	while iters:
		res = [next(i) for i in iters]
		yield tuple(res)

