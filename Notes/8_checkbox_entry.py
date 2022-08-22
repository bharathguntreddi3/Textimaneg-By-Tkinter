from tkinter import *

root = Tk()

root.geometry("644x344")

def getval():
    print("hello")

# heading
Label(root, text="welcome", font="Arial 15 bold", padx=15).grid(row=0,column=3)

# values for the form
name = Label(root, text="Name", )
phone = Label(root, text="phoen")
gender = Label(root, text="gender")
emergency = Label(root, text="emergency contact")
payment = Label(root, text="payment")

# packed to the object Tk root
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment.grid(row=5, column=2)

# entry variables to store the values
name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
emergency_value = StringVar()
payment_value = IntVar()

# different Entries 
name_entry = Entry(root, textvariable=name_value)
phone_entry = Entry(root, textvariable=phone_value)
gender_entry = Entry(root, textvariable=gender_value)
emergency_entry = Entry(root, textvariable=emergency_value)
payment_entry = Entry(root, textvariable=payment_value)

# Packing the Entries to the Tk object root
name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
emergency_entry.grid(row=4, column=3)
payment_entry.grid(row=5, column=3)

# checkbox
foodservice = Checkbutton(text="book your meals")
foodservice.grid(row=6, column=3)

# button and packing it andd assigning it a command
Button(text="submit", command=getval).grid(row=7, column=3)
root.mainloop()