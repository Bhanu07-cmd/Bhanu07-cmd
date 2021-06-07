from tkinter import *
import random

window = Tk()
window.title("Game")
window.geometry("1024x720")

Label(window, text="Rock, Paper, Scissors", bg='grey', font=50).pack()


user_choice = StringVar()
Label(window, text="choose any one: rock, paper, scissors", bg='orange').pack()
Entry(window, textvariable=user_choice).pack()

computer_choice = random.randint(1, 3)
if computer_choice == 1:
    computer_choice = "rock"
elif computer_choice == 2:
    computer_choice = "paper"
else:
    computer_choice = "scissors"

result = StringVar()


def play():
    user_pick = user_choice.get()
    if user_pick == computer_choice:
        result.set("tie, you both selected the same")
    elif user_pick == "rock" and computer_choice == "paper":
        result.set("you loose,computer select paper")
    elif user_pick == "paper" and computer_choice == "scissors":
        result.set("you win,computer select scissors")
    elif user_pick == "scissors" and computer_choice == "rock":
        result.set("you loose, computer selected paper")
    elif user_pick == "scissors" and computer_choice == "paper":
        result.set("you win, computer selected the paper")
    else:
        result.set("Invalid, choose any one -- rock, paper, scissors")


def reset():
    result.set("")
    user_choice.set("")


def exit():
    window.destroy()

Entry(window, font = 'arial 10 bold', textvariable = result, bg ='antiquewhite2',width = 50,).pack()

Button(window, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).pack()

Button(window, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = reset).pack()

Button(window, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = exit).pack()


window.mainloop()















window.mainloop()