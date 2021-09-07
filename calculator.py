import tkinter as tk
from tkinter import *

expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def press_equal():

    global expression
    try:
        total = str(eval(expression))
        print(total)
        equation.set(total)
        expression = ""

    except:
        equation.set("error")
        expression = ""


def to_clear():
    global expression
    expression = ""
    equation.set("")


def back():
    global expression
    expression = str(expression[:-1])
    equation.set(expression)





root = tk.Tk()
root.title('Calculator')
root.config(background = 'orange')
root.geometry('300x270')

#entry
equation = tk.StringVar()
entry = tk.Entry(root, textvariable = equation)
entry.pack(pady = (0,200) ,expand = True)
entry.grid(columnspan = 4,ipadx = 70 , ipady = 2)
entry.focus()

#buttons

button1 = tk.Button(root, text = '1', bg = 'yellow', height = 1, width = 5, command = lambda : press(1))
button1.grid(column = 0, row = 3, ipady = 1, pady = (30,2))

button2 = tk.Button(root,text = '2', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda : press(2))
button2.grid(column = 1, row = 3, ipady = 1, pady = (30,2))

button3 = tk.Button(root,text = '3', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda : press(3))
button3.grid(column = 2, row = 3, ipady = 1, pady = (30,2))

button4 = tk.Button(root,text = '4', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda : press(4))
button4.grid(column = 0, row = 4, ipady = 1, pady = (10,2))

button5 = tk.Button(root,text = '5', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda : press(5))
button5.grid(column = 1, row = 4, ipady = 1, pady = (10,2))

button6 = tk.Button(root,text = '6', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda : press(6))
button6.grid(column = 2, row = 4, ipady = 1, pady = (10,2))

button7 = tk.Button(root,text = '7', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda : press(7))
button7.grid(column = 0, row = 5, ipady = 1, pady = (10,2))

button8 = tk.Button(root,text = '8', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda : press(8))
button8.grid(column = 1, row = 5, ipady = 1, pady = (10,2))

button9 = tk.Button(root,text = '9', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda : press(9))
button9.grid(column = 2, row = 5, ipady = 1, pady = (10,2))

button0 = tk.Button(root,text = '0', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda : press(0))
button0.grid(column = 0, row = 6, ipady = 1, pady = (10,2))

minus = tk.Button(root,text = '-', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda : press('-'))
minus.grid(column = 3, row = 3, ipady = 1, pady = (30,2))


plus = tk.Button(root,text = '+', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda : press('+'))
plus.grid(column = 3, row = 4, ipady = 1, pady = (10,2))

mult = tk.Button(root,text = '*', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda : press('*'))
mult.grid(column = 3, row = 5, ipady = 1, pady = (10,2))

divide = tk.Button(root,text = '/', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda : press('/'))
divide.grid(column = 3, row = 6, ipady = 1, pady = (10,2))

decimal = tk.Button(root,text = '.', fg = 'black', bg = 'yellow', height = 1, width = 5, command = lambda: press('.'))
decimal.grid(column = 1, row = 6, ipady = 1, pady = (10,2))

equal = tk.Button(root,text = '=', fg = 'black', bg = 'yellow', height = 1, width = 5, command = press_equal)
equal.grid(column = 2, row = 6, ipady = 1, pady = (10,2))

clear = tk.Button(root,text = 'clear', fg = 'black', bg = 'yellow', height = 1, width = 5, command = to_clear)
clear.grid(column = 0, row = 7, ipady = 1, pady = (10,2))

back = tk.Button(root,text = 'back', fg = 'black', bg = 'yellow', height = 1, width = 5, command = back)
back.grid(column = 1, row = 7, ipady = 1, pady = (10,2))







root.mainloop()