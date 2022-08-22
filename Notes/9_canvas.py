from string import hexdigits
from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
can_width = Canvas(root, width=canvas_width, height=canvas_height)
can_width.pack()
root.mainloop()