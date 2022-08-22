from tkinter import *
import turtle

root = Tk()

def fun():
	print("hello world")
	# b = turtle.Turtle()

	# b.speed(100)

	# b.color("red", "yellow")

	# b.begin_fill()

	# for i in range(100):  #for loop for the number of iterations of lines
	# 	b.forward(100)
	# 	b.left(167)   #each iteration with 167 degrees

	# b.end_fill()  #color fill

	# b.hideturtle()

	# turtle.done()

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side="left", anchor="nw")

b1 = Button(frame, fg="red", text="print now", command=fun)
b1.pack(padx=20)

b1 = Button(frame, fg="red", text="print now")
b1.pack(padx=20)

b1 = Button(frame, fg="red", text="print now")
b1.pack(padx=20)

b1 = Button(frame, fg="red", text="print now")
b1.pack(padx=20)


root.mainloop()

