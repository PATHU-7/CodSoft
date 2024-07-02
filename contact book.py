import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Contact-Book")
root.geometry("300x550")
root.configure(bg='#EADDCA')
root.resizable(False, False)

contact_list = []

Name = StringVar()
N = Frame(root, width=100, height=40, bg='#F6F5F2')
N_entry = Entry(N, width=10, font="Corbel 20", bd=0, bg='#F6F5F2', textvariable=Name)
N_entry.focus()

Number = StringVar()
Nu = Frame(root, width=100, height=40, bg='#F6F5F2')
Nu_entry = Entry(Nu, width=26, font="Corbel 20", bd=0, bg='#F6F5F2', textvariable=Number)
Nu_entry.focus()

box = Frame(root, bd=1, width=200, height=330, bg="#F6F5F2")
box.place(x=20, y=150)
select = Listbox(box, font=('Corbel', 20), width=17, height=8, bg='#F6F5F2', cursor="hand2", selectbackground="#F3D0D7")
select.pack(side=LEFT, fill=BOTH, padx=2)
scroll = Scrollbar(box)
scroll.pack(side=RIGHT, fill=BOTH)
select.config(yscrollcommand=scroll.set)
scroll.config(command=select.yview)


def selected():
    try:
        return int(select.curselection()[0])
    except IndexError:
        return None


def add():
    if Name.get() and Number.get():
        contact_list.append([N_entry.get(), Nu_entry.get()])
        N_entry.delete(0, END)
        Nu_entry.delete(0, END)
        Select_set()


def edit():
    sel = selected()
    if sel is not None:
        contact_list[sel] = [N_entry.get(), Nu_entry.get()]
        N_entry.delete(0, END)
        Nu_entry.delete(0, END)
        Select_set()


def delete():
    sel = selected()
    if sel is not None:
        del contact_list[sel]
        Select_set()


def view():
    sel = selected()
    if sel is not None:
        NAME, PHONE = contact_list[sel]
        Name.set(NAME)
        Number.set(PHONE)


def clear():
    N_entry.delete(0, END)
    Nu_entry.delete(0, END)
    Select_set()


def Select_set():
    contact_list.sort()
    select.delete(0, END)
    for name, phone in contact_list:
        select.insert(END, name)


Select_set()

Label(root, text='NAME', font='Corbel 20 bold', bg='#EADDCA').place(x=10, y=10)
Entry(root, textvariable=Name, width=11, font="Corbel 20", bd=0, bg='#F6F5F2').place(x=115, y=10)

Label(root, text='PHONE', font='Corbel 20 bold', bg='#EADDCA').place(x=10, y=50)
Entry(root, textvariable=Number, width=11, font="Corbel 20", bd=0, bg='#F6F5F2').place(x=115, y=50)

Label(root, text='CONTACT-LIST', font='Corbel 20 bold', bg='#EADDCA').place(x=50, y=100)

Button(root, text="ADD", font='Corbel 15 bold', bg='white', command=add).place(x=47, y=447)
Button(root, text="EDIT", font='Corbel 15 bold', bg='white', command=edit).place(x=118, y=447)
Button(root, text="DELETE", font='Corbel 15 bold', bg='white', command=delete).place(x=65, y=500)
Button(root, text="VIEW", font='Corbel 15 bold', bg='white', command=view).place(x=190, y=447)
Button(root, text="CLEAR", font='Corbel 15 bold', bg='white', command=clear).place(x=165, y=500)

root.mainloop()
