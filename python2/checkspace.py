import sys
def isWhiteLine(st):
	if(st.strip())=='':
		return True

f=open(sys.argv[1],"r")
for line in f:
	if(not isWhiteLine(line)):
		print(line)
	
