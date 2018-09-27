import sys
import thread
import time
import queue

dataqueue=queue.Queue()
mutex=thread.allocate_lock()
l=len(sys.argv)-1
exitmutex=[False]*l
li1=[]
def filepro(fname,idn):
	#time.sleep(1)
	mutex.acquire()	
	c=0
	cw=0
	with open(fname,'r') as f1:
		for i in f1.readlines():
			if not i.strip()=='':
				c=c+1
			l1=i.split()
			cw=cw+len(l1)
		li1.append((fname,c,cw))
		#print('Total lines of {0} are {1} and words are {2}'.format(fname,c,cw))
	mutex.release()
	dataqueue.put(li1)
	exitmutex[idn]=True
def parent():
	i1=0
	if l==0:
		print('No files to read')
	else:
		for i in sys.argv[1:]:
			thread.start_new_thread(filepro,(i,i1))
			i1=i1+1
		while(False in exitmutex):pass
		data=dataqueue.get()
		for j in sorted(data):
			print("{0:15}\t{1:<5}\t{2:<5}".format(j[0],j[1],j[2]))
		#print('Exiting')
if __name__=='__main__':
	parent()
	
