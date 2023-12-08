
# create a button

import tkinter as tk

windows= tk.Tk()
windows.title("modified the title")

label= tk.Label(windows, text="Hello Beginner")
label.pack()

button= tk.Button(windows, text="this is a button")
button.pack(side='bottom')

windows.geometry("500x500")


windows.mainloop()