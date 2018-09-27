import threading

def tex(ar1):
	print('hello %s'%ar1)
def tex1(ar2):
	print('hello %s'%ar2)

ar1="first"
ar2="second"
t1=threading.Thread(target=tex,args=(iter(ar1)))
t2=threading.Thread(target=tex1,args=(iter(ar2)))
t1.start()
t2.start()
t1.join()
t2.join()
