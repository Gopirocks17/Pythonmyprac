import os,time

def child(pipeout):
	zzz=0
	while 1:
		time.sleep(zzz)
		os.write(pipeout,'spam %03d'%zzz)
		zzz=(zzz+1)%5


def parent():
	pipein,pipeout=os.pipe()
	if os.fork()==0:
		child(pipeout)
	else:
		while 1:
			line=os.read(pipein,32)
			print 'parent %d got %s at %s'%(os.getpid(),line,time.time())
parent()
