import random
import string
from tkinter import *
import pyperclip


def PassWord():
    letters = string.ascii_letters
    num = string.digits
    symbol = string.punctuation

    pas = []
    pl = int(length.get())

    for i in range(0, pl):
        pas += random.choices(letters + num + symbol)

    password = ''.join(pas)
    password_label.config(text="Generated Password ", fg='white', bg='black')
    password_label.password_text.config(text=password, fg="#00FF00")


def CopyPassword():
    passw = password_label.password_text.cget("text")
    pyperclip.copy(passw)


root = Tk()

root.title("password_generator")
root.geometry("300x320")
root.resizable(False,False)
root.config(bg="black")

label = Label(root,text="Password Generator",font="Corbel 20 bold",fg='white',bg='black')
label.place(x=35,y=5)

label1 = Label(root,text="Password Length",font="Corbel 15 bold",fg='white',bg='black')
label1.place(x=25,y=65)

length = Spinbox(root,from_=8,to=18,width=3,font=10,bg='white')
length.place_configure(x=200,y=70)


button = Button(root,text="Generate",bg='white',font="Corbel 15 bold",command=PassWord)
button.place(x=100,y=120)

password_label = Label(root,text="Generated Password ", font="Corbel 20 bold", fg='white', bg='black',)
password_label.place(x=30, y=180)

password_label.password_text = Label(root, text="", font="Corbel 20 bold", fg="blue", bg='black')
password_label.password_text.pack(side=BOTTOM,pady=60)

copy_button = Button(root, text="Copy", bg="white", font="Corbel 10 bold", command=CopyPassword)
copy_button.place(x=130, y=270)

root.mainloop()
