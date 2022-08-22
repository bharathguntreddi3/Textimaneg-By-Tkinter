from distutils.command.config import LANG_EXT
from email.mime import image
from tkinter import *
from PIL import Image, ImageTk
from zmq import INVERT_MATCHING

demo = Tk()

# png photos
# demo.geometry("500x400")
# photo = PhotoImage(file="images/1.png")
# photo_label = Label(image=photo)
# photo_label.pack()

# JPG photos
image = Image.open("images/2.jpg")
photo = ImageTk.PhotoImage(image)
phot_label = Label(image=photo)
phot_label.pack()


demo.mainloop()