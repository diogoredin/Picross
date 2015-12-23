# GUI

from tkinter import *

# Create a window
window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.geometry("500x500")
window.configure(bg='black')

photo = PhotoImage(file = '../resources/Title.png')
label = Label(window, image = photo)
label.pack()

window.mainloop()

