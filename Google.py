import webbrowser
from tkinter import *

hello = Tk()
hello.title("GUI to open Google Chrome")
hello.geometry('400x400')


def google():
    webbrowser.open("www.google.com")


label = Label(hello, text='Google', font=25).pack()
head = Label(hello, text="Bhanu Prakash").pack(side=BOTTOM)
button = Button(hello, text='click here', command=google, font=10).pack()

hello.mainloop()