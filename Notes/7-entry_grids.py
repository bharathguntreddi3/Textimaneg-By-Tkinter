from cgitb import text
from tkinter import *

root = Tk()

user = Label(root, text="username")
password = Label(root, text="password")
user.grid()
password.grid(row=2)

def getval():
    print(uservalue.get())
    print(passvalue.get())

# variables
# boolean, double, int, string

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=2, column=1)

button1 = Button(text="submit", command=getval)
button1.grid()

root.mainloop()