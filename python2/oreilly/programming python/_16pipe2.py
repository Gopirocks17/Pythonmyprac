import os,time

def child(pipeout):
	zzz=0
	while 1:
		time.sleep(zzz)
		os.write(pipeout,'spam %03d\n'%zzz)
		zzz=(zzz+1)%5

def parent():
	pipein,pipeout=os.pipe()
	if os.fork()==0:
		os.close(pipein)
		child(pipeout)
	else:
		os.close(pipeout)
		pipein=os.fdopen(pipein)
		while 1:
			line=pipein.readline()[:-1]
			print 'parent %d got %s at %s'%(os.getpid(),line,time.time())
parent()
