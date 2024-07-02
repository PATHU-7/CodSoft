from random import randint
import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Rock-Paper-Scissor")
root.geometry("600x400")
root.resizable(False,False)
root.configure(bg='white')

heading = Label(root,text="COMPUTER",font="Corbel 20 bold",fg="black",bg="white")
heading.place(x=70,y=3)

heading = Label(root,text="USER",font="Corbel 20 bold",fg="black",bg="white")
heading.place(x=420,y=3)

rock = ImageTk.PhotoImage(Image.open("img/rock.png"))
paper = ImageTk.PhotoImage(Image.open("img/paper.png"))
scissor = ImageTk.PhotoImage(Image.open("img/scissor.png"))

rock_img = Image.open("img/rock.png")
paper_img = Image.open("img/paper.png")
scissor_img = Image.open("img/scissor.png")

rock_resized = rock_img.resize((rock_img.width // 5, rock_img.height // 5))
paper_resized = paper_img.resize((paper_img.width // 5, paper_img.height // 5))
scissor_resized = scissor_img.resize((scissor_img.width // 5, scissor_img.height // 5))

rock_photo = ImageTk.PhotoImage(rock_resized)
paper_photo = ImageTk.PhotoImage(paper_resized)
scissor_photo = ImageTk.PhotoImage(scissor_resized)


def message(x):
    msg['text'] = x


def win(user,comp):
    if user == comp:
        message(" it's tie")
    elif user == "rock":
        if comp == "paper":
            message("you loose")
        else:
            message("you win")
    elif user == "paper":
        if comp == "scissor":
            message("you loose")
        else:
            message("you win")
    elif user == "scissor":
        if comp == "rock":
            message("you loose")
        else:
            message("you win")
    else:
        pass


a = ['rock', 'paper', 'scissor']


def change(x):
    bot = a[randint(0,2)]
    if bot == "rock":
        label.config(image=rock)
    elif bot == "paper":
        label.config(image=paper)
    else:
        label.config(image=scissor)

    if x == "rock":
        label1.config(image=rock)
    elif x == "paper":
        label1.config(image=paper)
    else:
        label1.config(image=scissor)

    win(x,bot)


button = tkinter.Button(root, image=rock_photo, bd=0, bg='white',command=lambda: change("rock"))
button.place(x=205, y=320)

button = tkinter.Button(root, image=paper_photo, bd=0, bg='white',command=lambda: change("paper"))
button.place(x=275, y=320)

button = tkinter.Button(root, image=scissor_photo, bd=0, bg='white',command=lambda: change("scissor"))
button.place(x=345, y=320)

label = Label(root, image=rock,bg='white')
label.place(x=25,y=35)

label1 = Label(root, image=rock,bg='white')
label1.place(x=340,y=35)

msg = Label(root,font="Corbel 20 bold",bg='white')
msg.place(x=250,y=250)


root.mainloop()
