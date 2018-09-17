import sys
def intersection((l1,r1),(l2,r2)):
	if(l2[0]>r1[0] or l1[0]>r2[0]):
		print("if1")
		return 
	if(r1[1]<l2[1] or r2[1]<l1[1]):
		print("if2")
		return
	if((l2[0]>l1[0] and r2[1]>r1[1])or(l1[0]>l2[0] and r1[1]>r2[1])):
		i1=(r1[0],l2[1])
		i2=(l2[0],r1[1])
		return (i1,i2)
	if((l2[0]>l1[0] and r2[1]<r1[1])or(l1[0]>l2[0] and r1[1]<r2[1])):
		i1=(l2[0],l1[1])
		i2=(r1[0],r2[1])
		return (i1,i2)
l1=(int(sys.argv[1]),int(sys.argv[2]))
r1=(int(sys.argv[3]),int(sys.argv[4]))
l2=(int(sys.argv[5]),int(sys.argv[6]))
r2=(int(sys.argv[7]),int(sys.argv[8]))
A=(l1,r1)
B=(l2,r2)
print(intersection(A,B))
	
	
	

