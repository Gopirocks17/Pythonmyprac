a = list(raw_input())
b = len(a)
print b
i=0
l=[]
while(i<b-1):
	c=1
	while(True):
        	if(a[i]==a[i+1]):
            		c=c+1
            		i=i+1
			if(i == b-1):
				l.append((c,int(a[i])))
				break
        	else:
            		l.append((c,int(a[i])))
            		i=i+1
            		print l
	    		break
for i in l:
    print i,
