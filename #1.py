from tkinter import *
from tkinter import ttk
import tkinter
import numpy as np
from PIL import ImageTk, Image
root=tkinter.Tk()
root.title("Мой приложения")
root.geometry("300x150")

def clicket():
    while True:
        e=entry.get()
        c=len(e)
        print(c)
        lbl2.config(text=c , font=25,background="blue")

button = Button(root,text="Рассчитать", font=2,command=clicket)
button.side=BOTTOM
button.grid(row=10,column=25,columnspan=20, padx=100, pady=10)
entry = Entry(root, font=30)
entry.side=RIGHT
entry.grid(row=0,column=25,columnspan=100, padx=30, pady=10)


lbl2=Label(root, text="РЕЗУЛЪТАТ")
lbl2.grid(row=8,column=25,columnspan=20, padx=10, pady=10)
root.mainloop()

