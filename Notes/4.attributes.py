from struct import pack
from textwrap import fill
from tkinter import *
from tkinter.font import BOLD

demo = Tk()

# Label options
# text = add text
# ad = background
# fg = foreground
# font = set font
# padx = x padding
# pady = y padding
# relief = border styling- sunken, raised, groove, ridge

title_label = Label(text = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                    when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                    It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
                    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
                    and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.''',
                    bg="red", fg="white", padx=50, pady=50, font="Arial  10 bold", borderwidth=3, relief=SUNKEN)
title_label.pack(anchor=CENTER, side=BOTTOM, fill = Y)

demo.mainloop()