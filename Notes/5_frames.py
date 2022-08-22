from tkinter import *
root = Tk()


f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y", pady=100)

f2 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill="x", padx=145)

l1 = Label(f1, text="frame1")
l1.pack()

l2 = Label(f2, text="frame2")
l2.pack()

root,mainloop()