'''
Author : Bharath Guntreddi
Date : 21/07/2022
'''

# from asyncore import file_dispatcher
import tkinter as tk
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfile, asksaveasfilename

window = tk.Tk()    # start GUI

window.title("GB Text Editor")
# to expand and contract naturally when the window is resized
window.rowconfigure(0, minsize=800, weight=1)      # row index from 0 to 800
window.columnconfigure(1, minsize=800, weight=1)    # clomn index from 1 to 800

'''
open_file() functon to open a file when we tap on the open button
'''
def open_file():
    # displaying a fileopen dialog box to open a file
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return     # if there are no files are selected thn return nothing, stay in the same window
    TextEdit.delete("1.0", tk.END)   # clears the content of edit box
    ''' open the file and read its content'''
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        TextEdit.insert(tk.END, text)
    window.title(f"GB Text Editor - {filepath}")    # again contains the path of the same file
#############################################################################

'''
save_file functon to save a file
'''
def save_file():
    # ask the user for the desired location to save the file
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("all Files", "*.*")])
    if not filepath:
        return      # return to same file with user cancels the program
    # create new file and extract from TextEdit with get() and assign to the variable
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = TextEdit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"GB Text Editor - {filepath}")

TextEdit = tk.Text(window, bg="black", fg="green")
# create frame for the open and save buttons
FrameButtons = tk.Frame(window, relief=tk.RAISED, bd=2, bg="black")
open_button = tk.Button(FrameButtons, text="Open", bg="black", fg="cyan", command=open_file)      # button for open
save_button = tk.Button(FrameButtons, text="Save As", bg="black", fg="cyan", command=save_file)   # button for save 
'''
Creating grid with two rows and one column ,
to put the open on the top of the Save As button ,
with exansion.
'''
open_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
save_button.grid(row=1, column=0, sticky="ew", padx=5)
# creating grid with one grid and two columns to pack them to the keft of the TextEditoe
FrameButtons.grid(row=0, column=0, sticky="ns")
TextEdit.grid(row=0, column=1, sticky="nsew")

window.mainloop()     # end GUI 🤞