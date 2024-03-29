#Create Menubar in Python GUI Application  
import tkinter as tk  
from tkinter import ttk  
from tkinter import Menu  
win = tk.Tk()  
win.title("Gesure control system")  
#Exit action  
def _quit():  
   win.quit()  
   win.destroy()  
   exit()  
#Create Menu Bar  
menuBar=Menu(win)  
win.config(menu=menuBar)  
#File Menu  
fileMenu= Menu(menuBar, tearoff=0)  
fileMenu.add_command(label="Exit", command=_quit)  
menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Video player control", command=_quit)
menuBar.add_cascade(label="Slides control", command=_quit)  
#Help Menu  
helpMenu= Menu(menuBar, tearoff=0)  
helpMenu.add_command(label="About")  
menuBar.add_cascade(label="Help", menu=helpMenu)  
#Calling Main()  
win.mainloop()  