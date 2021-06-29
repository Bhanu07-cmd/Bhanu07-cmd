from tkinter import *


def add():
    res = int (e1.get()) + int (e2.get())
    number.set(res)


def sub():
    res = int (e1.get()) - int (e2.get())
    number.set(res)


def mul():
    res = int (e1.get()) * int (e2.get())
    number.set(res)


def div():
    res = int (e1.get()) / int (e2.get())
    number.set(res)




window = Tk()

window.geometry('500x500')
number = StringVar()
Label(window, text='Enter first Number: ', font=10).grid(row=0, column=0)
Label(window, text='Enter second Number: ', font=10).grid(row=1, column=0)
Label(window, text='Result: ', font=10, background='grey').grid(row=2, column=0)
result = Entry(window, textvariable=number).grid(row=2, column=1)


e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

a = Button(window, text='add',  command=add, padx=2).grid(row=4, column=0)
s = Button(window, text='sub', command=sub).grid(row=5, column=0)
m = Button(window, text='Mul', command=mul).grid(row=4, column=1)
d = Button(window, text='Div', command=div).grid(row=5, column=1)

window.mainloop()