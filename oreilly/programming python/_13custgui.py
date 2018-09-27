from tkinter import *
from tkinter.messagebox import showinfo
from _11tkin import mygui

class custgui(mygui):
	def reply(self):
		showinfo(title='custgui',message='different')
if __name__ == '__main__':
	custgui().pack()
	mainloop()
