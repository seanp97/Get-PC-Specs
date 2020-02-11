import platform
import os
from tkinter import *
import sys
import tkinter
from tkinter import messagebox

def getSpecs():
    pm = platform.machine()
    pv = platform.version()
    pp = platform.platform()
    pu = platform.uname()
    ps = platform.system()
    ppr = platform.processor()
    messagebox.showinfo('Specs', "Platform Machine: " + pm + "\n" + "Platform Version: " + pv + "\n" + "Platform : " + pp + "\n" + "Operating System: " + ps + "\n" + "Operating Processor: " + ppr + "\n")

app = Tk()
app.geometry("800x400")
app.title("Your PC Specs")

pcLabel = Label(app, text="Click button to find out your PC specs",  padx=20, pady=20, font='Helvetica 14 bold')
pcLabel.grid(column=0, row=0)
pcBtn = Button(app, bd=3, text="Get Specs", command=getSpecs)
pcBtn.grid(column=0, row=1)

app.mainloop()