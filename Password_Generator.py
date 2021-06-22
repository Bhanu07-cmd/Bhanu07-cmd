from tkinter import *
import random, string
import pyperclip


window = Tk()
window.geometry('1023x720')
window.title("Password Generator")

Label(window, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
Label(window, text='Data flair', font='arial 15 bold').pack(side=BOTTOM)

pass_label = Label(window, text="PASSWORD LENGHT", font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(window, from_ = 4, to_ = 8, textvariable = pass_len, width=15).pack()


pass_str = StringVar()


def Generator():
    password = ''

    for x in range(0, 4):
        Password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
        for y in range(pass_len.get()-4):
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
            pass_str.set(password)


Button(window, text="GENERATE PASSWORD", command=Generator).pack(pady=5)
Entry(window, textvariable= pass_str).pack()


def copy_password():
    pyperclip.copy(pass_str.get())


Button(window, text='COPY TO CLIPBOARD', command=copy_password).pack(pady=5)

window.mainloop()