# GUI

from tkinter import *

# Create a window
window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.geometry("500x500")
window.configure(bg='black')

# Create a canvas
c = Canvas(window, height = 75, width = 300)
filename = PhotoImage(file = '../resources/Title.png')
image = c.create_image(32.5, 150, anchor=NE, image = filename)

c.pack()
window.mainloop()

