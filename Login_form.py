from tkinter import *
from functools import partial


def login(username, password):
    print("Username Entered: ", username.get())
    print("Password Enterd: ", password.get())

window = Tk()
window.title("Login Form")
window.geometry('400x400')

usernamelabel = Label(window, text='Username').grid(row=0, column=0)
username = StringVar()
usernameentry = Entry(window, textvariable=username).grid(row=0, column=1)


passwordlabel = Label(window, text='Password').grid(row=1, column=0)
password = StringVar()
passwordentry = Entry(window, textvariable=password).grid(row=1, column=1)


login = partial(login, username, password)

loginbutton = Button(window, text='Login', command=login).grid(row=2, column=1)


window.mainloop()
