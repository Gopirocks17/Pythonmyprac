import textwrap
import sys
f=open(sys.argv[1],"r")
w=int(sys.argv[2])
t1=[]
for i in f:
	l=(textwrap.wrap(i,width=w))
	t1.extend(l)
le=len(t1)
print le
j=0
while(j<le):
	print t1[j]
	j=j+1
