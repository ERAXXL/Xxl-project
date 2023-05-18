from tkinter import *
from tkinter import ttk
import numpy as np
import tkinter
import numpy as np


def clicket():
    e1=entry1.get()
    e2=entry2.get()
    c=np.random.randint(e1,e2)
    lbl3.config(text=c , font=25,background="blue")
    print(c)

root=tkinter.Tk()
root.title("Мой приложения")
root.geometry("800x500")



button = Button(root,text="СГЕНЕРИРОВАТЬ", font=0,command=clicket)
button.side=BOTTOM
button.grid(row=7,column=15,columnspan=10, padx=5, pady=5)
lbl=Label(root,font=25, text="                    ВЫБИРАЙ     ЦИФРЫ \n ОТ                                                                                              ДО ")
lbl.grid(row=1,column=10,columnspan=1, padx=5, pady=5)
entry1 = Entry(root, font=1)
entry1.side=RIGHT
entry1.grid(row=2,column=0,columnspan=20, padx=5, pady=5)
entry2 = Entry(root, font=1)
entry2.side=LEFT
entry2.grid(row=2,column=20,columnspan=20, padx=3, pady=3)
lbl2=Label(root, text="РЕЗУЛЪТАТ")
lbl2.grid(row=8,column=10,columnspan=1, padx=5, pady=5)
lbl3=Label(root, )
lbl3.grid(row=10,column=10,columnspan=20, padx=3, pady=3)
root.mainloop()


