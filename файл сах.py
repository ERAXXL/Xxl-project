from tkinter import *
from tkinter import ttk
import numpy as np
import tkinter


root=tkinter.Tk()
root.title("Мой приложения")
root.geometry("800x500")

los=[]
def inp():
    text = entry.get()

    # Открыть файл для записи (если файл не существует, он будет создан)
    with open("text.txt", "w") as file:
    # Записать текст в файл
        file.write(text)

# Закрыть файл
    file.close()

def inp1():
    text = entry.get()
    for i in text:
        if i in "a":
            i="а"
        else:
            i=i
    # Открыть файл для записи (если файл не существует, он будет создан)
        with open("text.txt", "a") as file:
    # Записать текст в файл
            file.write(i)

    # Закрыть файл
    file.close()





button = Button(root,text="Сохронить", font=0,command=inp)
button.side=BOTTOM
button.grid(row=4,column=10,columnspan=20, padx=300, pady=40)

button2 = Button(root,text="Обновить", font=0,command=inp1)
button2.side=BOTTOM
button2.grid(row=3,column=10,columnspan=20, padx=300, pady=40)


lbl=Label(root,font=25, text="Текст для сохранения")
lbl.grid(row=1,column=10,columnspan=20, padx=300, pady=40)

entry = Entry(root, font=1)
entry.side=RIGHT
entry.grid(row=2,column=10,columnspan=20, padx=300, pady=40)

root.mainloop()