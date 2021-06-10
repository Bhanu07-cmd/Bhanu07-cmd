from _ast import Lambda
from tkinter import *

cal = Tk()
cal.title("Calculator using GUI")
cal.geometry("1024x720")

ent = Entry(cal, width=35, borderwidth=5)
ent.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = ent.get()
    ent.delete(0, END)
    ent.insert(0, str(current) + str(number))


def button_clear():
    ent.delete(0, END)


def button_add():
    first_number = ent.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    ent.delete(0, END)


def button_sub():
    first_number = ent.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    ent.delete(0, END)


def button_mul():
    first_number = ent.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    ent.delete(0, END)


def button_div():
    first_number = ent.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    ent.delete(0, END)



def button_equal():
    second_number = ent.get()
    ent.delete(0, END)

    if math == "addition":
        ent.insert(0, f_num + int(second_number))

    if math == "subtraction":
        ent.insert(0, f_num - int(second_number))

    if math == "multiplication":
        ent.insert(0, f_num * int(second_number))

    if math == "division":
        ent.insert(0, f_num % int(second_number))


button_1 = Button(cal, text="1", bg="grey", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(cal, text="2", bg="grey", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(cal, text="3", bg="grey", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(cal, text="4", bg="grey", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(cal, text="5", bg="grey", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(cal, text="6", bg="grey", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(cal, text="7", bg="grey", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(cal, text="8", bg="grey", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(cal, text="9", bg="grey", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(cal, text="0", bg="grey", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(cal, text="+", bg='orange', padx=39, pady=20, command=button_add)
button_equal = Button(cal, text="=", bg='orange', padx=40, pady=20, command=button_equal)
button_clear = Button(cal, text="clear", bg='orange', padx= 30, pady=20, command=button_clear)
button_sub = Button(cal, text="-", bg='orange', padx=40, pady=20, command=button_sub)
button_mul = Button(cal, text="*", padx=40, pady=20, command=button_mul)
button_div = Button(cal, text="%", padx=39, pady= 20, command=button_div)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_clear.grid(row=5, column=2)
button_sub.grid(row=5, column=1)
button_mul.grid(row=4, column=0)
button_div.grid(row=5, column=0)












cal.mainloop()