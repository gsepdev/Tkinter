

#This is a basic Tkinter script that creates a simple window with a message.

import tkinter as tk

#create the main windows

window = tk.Tk()

#Create the lable with the message

label=tk.Label(window, text="Hello, Tkinter!")

#pack the label into the window

label.pack()

#start the main loop of the application
window.mainloop()