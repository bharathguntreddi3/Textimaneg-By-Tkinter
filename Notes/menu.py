# from cProfile import label
from cProfile import label
from tkinter import *
from turtle import color

root = Tk()

# root.geometry("500x400")

# # Non drop down menu
# # mymenu = Menu(root)
# # mymenu.add_command(label="File")
# # mymenu.add_command(label="Exit",command=quit)
# # root.config(menu=mymenu)

# yourmenu = Menu(root)

# m1 = Menu(yourmenu, tearoff=0)


# m1.add_command(label="project")
# m1.add_separator()
# m1.add_command(label="Save")
# m1.add_separator()
# m1.add_command(label="save as")
# m1.add_separator()
# m1.add_command(label="print")

# yourmenu.add_cascade(label="File",menu=m1)
# # yourmenu.add_command(label="Exit", command=quit)
# root.config(menu=yourmenu)


# # m2 = Menu(yourmenu, tearoff=0)


# # m2.add_command(label="project")
# # m2.add_separator()
# # m2.add_command(label="Save")
# # m2.add_separator()
# # m2.add_command(label="save as")
# # m2.add_separator()
# # m2.add_command(label="print")

# # yourmenu.add_cascade(label="File",menu=m2)
# # # yourmenu.add_command(label="Exit", command=quit)
# # root.config(menu=yourmenu)

mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0, bg="grey")
m1.add_command(label="new project")
m1.add_separator()
m1.add_command(label="save")
m1.add_separator()
m1.add_command(label="save as")
m1.add_separator()
m1.add_command(label="exit")
mainmenu.add_cascade(label="Files",menu=m1)
mainmenu.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)

root.mainloop()
