import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x500")
root.configure(bg='#EADDCA')
root.resizable(False,False)

task_list = []


def addtask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("task_list.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        list_box.insert(END,task)


def deletetask():
    global task_list
    task = str(list_box.get(ANCHOR))
    if task in task_list:
       task_list.remove(task)
       with open("task_list.txt",'w') as taskfile:
           for task in task_list:
               taskfile.write(task+"\n")
       list_box.delete(ANCHOR)


def openfile():

    try:
        global task_list
        with open("task_list.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                list_box.insert(END,task)

    except:
        file = open("task_list.txt","w")
        file.close()


icon = PhotoImage(file="img/task.png")
root.iconphoto(False,icon)

heading = Label(root,text="TASK-LIST",font="Corbel 20 bold",fg="black",bg="#EADDCA")
heading.place(x=130,y=15)

frame = Frame(root,width=380,height=40,bg='#F6F5F2')
frame.place(x=10,y=390)

task = StringVar()
task_entry = Entry(frame,width=26,font="Corbel 20",bd=0,bg='#F6F5F2')
task_entry.place(x=10,y=5)
task_entry.focus()

delete = PhotoImage(file="img/delete_.png")
width, height = delete.width(), delete.height()
delete = delete.subsample(15)
button = tkinter.Button(root, image=delete, bd=0, bg='#EADDCA',command=deletetask)
button.place(x=300, y=450)

add = PhotoImage(file="img/add.png")
add = add.subsample(13)
button = tkinter.Button(root, image=add, bd=0, bg='#EADDCA',command=addtask)
button.place(x=80, y=448)

box = Frame(root,bd=3,width=350,height=330,bg="#F6F5F2")
box.pack(pady=(70,0))
list_box = Listbox(box,font=('Corbel',20),width=23,height=8,bg='#F6F5F2',cursor="hand2",selectbackground="#F3D0D7")
list_box.pack(side=LEFT,fill=BOTH,padx=2)
scroll = Scrollbar(box)
scroll.pack(side=RIGHT,fill=BOTH)
list_box.config(yscrollcommand=scroll.set)
scroll.config(command=list_box.yview)

openfile()

root.mainloop()
