
'''
import string

f=open('textsa1','w')
print(list(string.lowercase))
for i in list(string.lowercase):
	f.write(i+"\n")
f.close()

o/p:
a
b
c
...
'''

'''
#2
a=[1,2,3]
b=(4,5,6)
for i,j in zip(a,b):
	print i+j
o/p 5 
7
9
'''

'''
#3
import string
f=open('textsa1','w')
l=string.lowercase
i=0
while(i<len(l)):
	f.write(l[i:i+3]+"\n")
	i=i+3
f.close()
o/p 
abc
def
...
'''

'''
#4
import string
l='abc'
for i in l:
	f=open(i+".txt",'w')
	f.write(i)
f.close()
'''

'''
#5
a=[1,2,3]
for i,j in enumerate(a):
	print("Item {0} has index {1}".format(j,i)) 
'''

'''
#6
d= dict(weather="clima",earth="terra",rain="chuva")
inp=raw_input("Enter word: ")
try:
	print d[inp]
except KeyError:
	print "that word doesn't exist"
'''
'''
#7
import requests
r= requests.get("http://www.pythonhow.com/data/universe.txt")
t=r.text
ca=t.count('a')
print t
print ca
'''
'''
#8
import webbrowser
query=raw_input("Enter your search query")
print (type(query))
url="https://www.google.co.in/search?ei=Ftb3Wv6BH4TovATnn5zwDg&q={0}".format(query)
webbrowser.open_new(url)
'''

'''
#9
import pandas as pd
da=pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
da=da*2
da.to_csv("samplec.csv",index=None)
'''

'''
#10
import pandas as pd
import pylab as plt
da= pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
da.plot(x='x',y='y',kind='scatter')
plt.show()
'''
'''
#11
import datetime
print("Today is"+datetime.datetime.now())
'''

'''
#12 password generator
import random
import string
alnum= string.lowercase+string.uppercase+'0123456789'+'!@#$%^&*()?'
print(''.join(random.sample(alnum,6)))
'''

'''
#13 password checker

sp='!@#$%^&*'
while True:
	ps=raw_input("Enter password ")
	d=any([i.isdigit() for i in ps])
	u=any([i.isupper() for i in ps])
	l=len(ps)>=5
	s=any([i in sp for i in ps])
	if(d and u and l and s):
		print('password is fine')
		break
	else:
		if not d:
			print("The password should have atleast one digit")
		if not u:
			print("The password should have atleast one uppercase")
		if not l:
			print("The password length should be more than 4 ")
		if not s:
			print("The password should have atleast one special case")
'''

'''
#14 username and password
l=[]
sp='!@#$%^&*'
f=open('users.txt','r')
for i in f:
	st=i.strip()
	l.append(st)
f.close()
print l	
while True:
	un=raw_input("Enter Username: ")
	if(un not in l):
		print("Username is fine")
		break
	else:
		print("Username exists")
while True:
	ps=raw_input("Enter password: ")
	d=any([i.isdigit() for i in ps])
	u=any([i.isupper() for i in ps])
	l=len(ps)>=5
	s=any([i in sp for i in ps])
	if(d and u and l and s):
		print('password is fine')
		break
	else:
		if not d:
			print("The password should have atleast one digit")
		if not u:
			print("The password should have atleast one uppercase")
		if not l:
			print("The password length should be more than 4 ")
		if not s:
			print("The password should have atleast one special case")
'''

'''
#15 screeninfo
from screeninfo import get_monitors
 
width=get_monitors()[0].width
height=get_monitors()[0].height
 
print("Width: %s,  Height: %s" % (width, height))
'''

'''
#16 pyglet
import pyglet
window=pyglet.window.Window()
l=pyglet.text.Label('Hello world',font_name='Times New Roman',font_size=34,x=window.width//2,y=window.height//2,anchor_x='center',anchor_y='center')

@window.event
def on_draw():
	window.clear()
	l.draw()

pyglet.app.run()
'''

'''
#17 ignore spaces and other strings

f=open('countries-raw.txt','r')
c=f.readlines()
g=open('newcountries.txt','w') 
for i in c:
	st=i.strip()
	if(st=='Top of Page' or len(st)==0 or len(st)==1):
		pass
	else:
		g.write(st+"\n")
g.close()
f.close()
'''

'''
#18 filter countries
u=[]
ch = ["Portugal", "Germany", "Munster", "Spain"]
f=open("newcountries.txt",'r')
c=f.readlines()
f.close()
for i in c:
	st1=i.strip()
	u.append(st1)
u1=[i for i in ch for j in u if(i==j)]
print u1
'''

'''
#19 csv data
import pandas as pd

data=pd.read_csv("countries-by-area.txt")
data['density']=data['population_2013']/data['area_sqkm']
data=data.sort_values(by='density',ascending=False)
for i,r in data[:5].iterrows():
	print r['country']
'''

'''
#20 database file
import sqlite3

conn=sqlite3.connect("database.db")
cur=conn.cursor()
cur.execute("Select country from countries where area>2000000")
rows=cur.fetchall()
for i in rows:
	print i[0]
conn.close()
'''


'''
#21 database
import sqlite3
import pandas as pd
conn=sqlite3.connect("database.db")
curs=conn.cursor()
curs.execute("select* from countries where area >=2000000")
rel=curs.fetchall()
conn.close()
df= pd.DataFrame.from_records(rel)
df.columns=["Rank","Country","Area","Population"]
df.to_csv("csv12.csv",index=None)
'''

#22 GUI Programming
from tkinter import *
window=Tk()
file=open("Gui.txt",'a+')

def add():
	file.write(user_value.get()+"\n")
	entry.delete(0,END)
def save():
	global file
	file.close()
	file=open("Gui.txt",'a+')
def close():
	file.close()
	window.destroy()
user_value=StringVar()
entry=Entry(window,textvariable=user_value)
entry.grid(row=0,column=0)
button_add=Button(window,text='Add line',command=add)
button_add.grid(row=0,column=1)
button_add=Button(window,text='save',command=save)
button_add.grid(row=0,column=2)
button_add=Button(window,text='save and close',command=close)
button_add.grid(row=0,column=3)
window.mainloop()
































