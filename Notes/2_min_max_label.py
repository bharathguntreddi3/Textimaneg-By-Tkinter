from cProfile import label
from cgitb import text
from tkinter import *
from unittest.case import doModuleCleanups

demo = Tk()

demo.geometry("300x300")

demo.maxsize(600, 500)

demo.minsize(200, 200)

label1 = Label(text="Hello Welcome to Tkinter GUI")
label1.pack()



demo.mainloop()