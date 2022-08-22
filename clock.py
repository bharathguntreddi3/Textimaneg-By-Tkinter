from tkinter import *
from time import *

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("arial", 80), background="black", foreground="cyan")
label.pack(anchor='center')

time()
mainloop()