#import tkinter module
from tkinter import*

#create gui window

window=Tk()

#add widgets
#Name
l=Label(window,text="User Name :")
l.grid(row=1,cloumn=1)

e=Entry(window)
e.grid(row=1,column=2)

#mainloop
window.mainloop() 
