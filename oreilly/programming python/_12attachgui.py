from tkinter import *
from _11tkin import mygui

mainwin=Tk()
Label(mainwin,text=__name__).pack()

popup = Toplevel()
Label(popup,text='Attach').pack(side=LEFT)
mygui(popup).pack(side=RIGHT)
mainwin.mainloop()





