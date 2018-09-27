import sys


f=open(sys.argv[1],"r")
contents=f.read()
l=contents.split()
s1=set(l)
dc={}
for i in s1:
	cnt1=i.count('a')+i.count('e')+i.count('i')+i.count('o')+i.count('u')
	dc[i]=cnt1

l1=[[v,k] for k,v in dc.items() if v==max(dc.values())]
for k,v in l1:
	print("{0} {1}".format(k,v))

	
