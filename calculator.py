#Importing the tkinter library
from tkinter import *

#Functions for all the buttons

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        expression = "error! "
        equation.set(expression)
def clear():
    global expression
    expression = ""
    equation.set(expression)
#Defining a window
root = Tk()

#Naming the title of the app
root.title("Calculator")

#Setting the size of the window
root.geometry("290x100")
#Just set an image with photoimage lib
frame = Frame(root,highlightcolor="blue")
frame.grid(column=0,row=0,sticky=(N,W,E,S))


#Creating Buttons
equation = StringVar()
entry = Entry(frame,width=15,bg="light green",textvariable=equation).grid(row=2,column=4)
btn7 = Button(frame,text="7",width=5,bg="red",command=lambda: press(7)).grid(row=2,column=0)
btn8 = Button(frame,text="8",width=5,bg="red",command=lambda: press(8)).grid(row=2,column=1)
btn9 = Button(frame,text="9",width=5,bg="red",command=lambda: press(9)).grid(row=2,column=2)
btnd = Button(frame,text="/",width=5,bg="red",command=lambda: press("/")).grid(row=2,column=3)
btn4 = Button(frame,text="4",width=5,bg="red",command=lambda: press(4)).grid(row=3,column=0)
btn5 = Button(frame,text="5",width=5,bg="red",command=lambda: press(5)).grid(row=3,column=1)
btn6 = Button(frame,text="6",width=5,bg="red",command=lambda: press(6)).grid(row=3,column=2)
btnm = Button(frame,text="x",width=5,bg="red",command=lambda: press("*")).grid(row=3,column=3)
btn1 = Button(frame,text="1",width=5,bg="red",command=lambda: press(1)).grid(row=4,column=0)
btn2 = Button(frame,text="2",width=5,bg="red",command=lambda: press(2)).grid(row=4,column=1)
btn3 = Button(frame,text="3",width=5,bg="red",command=lambda: press(3)).grid(row=4,column=2)
btnmi = Button(frame,text="-",width=5,bg="red",command=lambda: press("-")).grid(row=4,column=3)
btn0 = Button(frame,text="0",width=5,bg="red",command=lambda: press(0)).grid(row=5,column=0)
btndot = Button(frame,text=".",width=5,bg="red",command=lambda: press(".")).grid(row=5,column=1)
btnpl = Button(frame,text="+",width=5,bg="red",command=lambda: press("+")).grid(row=5,column=2)
btnclear = Button(frame,text="clear",width=5,bg="light blue",command=clear).grid(row=3,column=4)
btneq = Button(frame,text="=",width=5,bg="red",command=equal).grid(row=5,column=3)




#The mainloop thing prevents closing of the window
root.mainloop()