#Importing the tkinter library
from tkinter import *

#Defining a window
root = Tk()

#Naming the title of the app
root.title("Calculator")

#Setting the size of the window
root.geometry("300x300")

#Just set an image with photoimage lib
bg = PhotoImage(file="black.v1.png")


#Creating a label to display image
label1 = Label(root,image=bg).pack()


#The mainloop thing prevents closing of the window
root.mainloop()