from random import*
from tkinter import *
from tkinter import ttk
import tkinter
import numpy as np


root=tkinter.Tk()
root.title("Мой приложения")
root.geometry("300x150")

def hack():
    q=[]
    s = entry.get().lower()
    n=int(entry2.get())
    for i in range(len(s)):
        if s[i] in ',."!':
            q.append(s[i])
            continue
        a = ord(s[i])+n 
        if 97<=a<=122:
            q.append((chr(a)))
            continue
        if a>122:
            q.append((chr(96 + (a-122))))
            continue
    
    lbl2.config(text=q,font=35)   
    print(*q,sep='')


button = Button(root,text="Шифровка", font=2,command=hack)
button.side=BOTTOM
button.grid(row=10,column=25,columnspan=20, padx=100, pady=10)
entry = Entry(root, font=30, text="Слова")
entry.side=RIGHT
entry.grid(row=0,column=25,columnspan=100, padx=30, pady=1)

entry2 = Entry(root, font=30, text="ключ")
entry2.side=RIGHT
entry2.grid(row=5,column=25,columnspan=20, padx=30, pady=10)

lbl2=Label(root, text="РЕЗУЛЪТАТ")
lbl2.grid(row=8,column=25,columnspan=20, padx=10, pady=10)
root.mainloop()
