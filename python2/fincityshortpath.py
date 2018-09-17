ans=[]
a=int(raw_input())
for _ in range(a):
	l=[]
	s=[]
	k=0
	ts=0
	b=int(raw_input())
	c=map(int,raw_input().split())
	for i in range(b):
		l.append(c[i])	
	l.sort()
	while(k<b):
		if(b==1):
			ts=s[0]
			break
		#elif(k==0):
		#	st=s[k]+s[k+1]
		#	ts=st
		#	k=k+2
		else:
			if(k==0):
				st=s[k]+s[k+1]
			else:
				st=st+s[k]
				ts=ts+st
				k=k+1
	ans.append(ts)
for i in ans:
	print("{0}".format(i))			
