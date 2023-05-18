from random import*
from tkinter import *
from tkinter import ttk
import tkinter
import numpy as np

root=tkinter.Tk()
root.title("Мой приложения")
root.geometry("300x150")

num = randrange(1, 100)
def clicket():
    num1=int(entry.get())
    
    print(num)
    if num == num1:
        c=('Вы угадали, поздравляем!')
                
    elif num1 < num:
        c=('Слишком мало, попробуйте еще раз')
    else:
        c=('Слишком много, попробуйте еще раз')
    lbl2.config(text=c , font=25,background="blue")

button = Button(root,text="Угадать", font=2,command=clicket)
button.side=BOTTOM
button.grid(row=10,column=25,columnspan=20, padx=100, pady=10)
entry = Entry(root, font=30)
entry.side=RIGHT
entry.grid(row=0,column=25,columnspan=100, padx=30, pady=1)


lbl2=Label(root, text="РЕЗУЛЪТАТ")
lbl2.grid(row=8,column=25,columnspan=20, padx=10, pady=10)
root.mainloop()

