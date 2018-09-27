'''a=int(raw_input())
b=raw_input().split(' ')
c=int(raw_input())
d=raw_input().split(' ')
l=(set(b).difference(set(d)) | set(d).difference(set(b)))
lm=map(int,l)
for i in sorted(lm):
    print(i)
'''
l=[]
s=0
a=map(int,raw_input().split(' '))
for i in range(a[1]):
    b=map(int,raw_input().split(' '))
    l.append(max(b[1:b[0]+1]))
for i in l:
    s=s+(i*i)
o=s%a[1]
print(o)
