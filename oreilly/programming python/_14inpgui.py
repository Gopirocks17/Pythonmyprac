from tkinter import *
from tkinter.messagebox import showinfo

def reply(name,age):
	showinfo(title='popup',message='hello %s and age is %d'%(name,age))

top = Tk()
top.title('Echo')

Label(top,text='Enter your name').pack(side=TOP)
ent=Entry(top)
ent.pack(side=TOP)
Label(top,text='Enter your age').pack(side=TOP)
ent1=Entry(top)
ent1.pack(side=TOP)
button=Button(top,text='Submit',command=(lambda:reply(ent.get(),int(ent1.get()))))
button.pack(side=LEFT)
top.mainloop()
