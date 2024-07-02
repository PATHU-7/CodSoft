from tkinter import *

root = Tk()

root.title("Calculator")
root.geometry("334x352")
root.resizable(False,False)
root.config(bg='black')

eqn = ""


def show(value):
    global eqn
    eqn += value
    label.config(text=eqn)


def clear():
    global eqn
    eqn = ""
    label.config(text=eqn)


def Del():
    global eqn
    eqn = eqn[:-1]
    label.config(text=eqn)


def calculate():
    global eqn
    try:
        result = str(eval(eqn))
        label.config(text=result)
        eqn = result
    except:
        label.config(text="Error")
        eqn = ""


label = Label(root,width=25,height=1,text="",font=("corbel",30),bg='black',fg='white')
label.pack()

Button(root,text='C',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',bg='#F30A49',command=lambda: clear()).place(x=10,y=65)
Button(root,text='%',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('%')).place(x=91,y=65)
Button(root,text='/',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('/')).place(x=172,y=65)
Button(root,text='DEL',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',bg='#FFF455',command=lambda: Del()).place(x=253,y=65)

Button(root,text='7',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('7')).place(x=10,y=122)
Button(root,text='8',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('8')).place(x=91,y=122)
Button(root,text='9',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('9')).place(x=172,y=122)
Button(root,text='*',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('*')).place(x=253,y=122)

Button(root,text='4',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('4')).place(x=10,y=179)
Button(root,text='5',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('5')).place(x=91,y=179)
Button(root,text='6',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('6')).place(x=172,y=179)
Button(root,text='+',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('+')).place(x=253,y=179)

Button(root,text='1',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('1')).place(x=10,y=236)
Button(root,text='2',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('2')).place(x=91,y=236)
Button(root,text='3',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('3')).place(x=172,y=236)
Button(root,text='-',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('-')).place(x=253,y=236)

Button(root,text='0',width=11,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('0')).place(x=10,y=293)
Button(root,text='.',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',command=lambda: show('.')).place(x=172,y=293)
Button(root,text='=',width=5,height=1,font=("corbel",18,'bold'),bd=1,fg='black',bg='#3DC2EC',command=lambda: calculate()).place(x=253,y=293)

root.mainloop()
