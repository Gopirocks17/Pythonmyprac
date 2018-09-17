#using oop for GUI
from tkinter import *
from tkinter.messagebox import showinfo

class mygui(Frame):
	def __init__(self,parent=None):
		Frame.__init__(self,parent)
		button=Button(self,text='Press',command=self.reply)
		button.pack()
	def reply(self):
		showinfo(title='pop up',message='pressed')
if __name__ == '__main__':
	window=mygui()
	window.pack()
	window.mainloop()
