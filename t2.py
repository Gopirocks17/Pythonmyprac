n=map(int,raw_input().split(' '))
arr=raw_input().split(' ')
h=raw_input().split(' ')
nh=raw_input().split(' ')
i=0
hc=0
while(i>n[1]+1):
    if h[i] in arr:
        hc=hc+1
        i+=1
    print(hc)
i=0
while(i>n[1]+1):        
    if nh[i] in arr:
        hc=hc-1
        i+=1
    print(hc)
print(hc)
        
