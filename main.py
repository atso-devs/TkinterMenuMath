import math
import tkinter as tk
from tkinter import *
import numpy as np

window = Tk()
window.title("")
window.geometry('500x200')

A = StringVar()
B = StringVar()


def ClkPlus():

    a = float(A.get())
    b = float(B.get())
    res = a + b
    textRes.configure(text="Результат: \n" + str(res))

def ClkMinus():

    a = float(A.get())
    b = float(B.get())
    res = a - b
    textRes.configure(text="Результат: \n" + str(res))

def ClkDiv():
    a = float(A.get())
    b = float(B.get())
    res = a / b
    textRes.configure(text="Результат: \n" + str(res))

def ClkMult():

    a = float(A.get())
    b = float(B.get())
    res = a * b
    textRes.configure(text="Результат: \n" + str(res))


mainmenu = Menu(window)
window.config(menu=mainmenu)


menuFunc = Menu(mainmenu, tearoff=0)

menuFunc.add_command(label='Сложить', command=ClkPlus)
menuFunc.add_command(label='Вычесть', command=ClkMinus)
menuFunc.add_command(label='Делить', command=ClkDiv)
menuFunc.add_command(label='Умножить', command=ClkMult)

mainmenu.add_cascade(label='Действия', menu=menuFunc)

textA = Label(window, text="A")
textA.grid(column=0, row=1)
txtInpA = Entry(window, width=15, textvariable=A)
txtInpA.grid(column=0, row=2)

textB = Label(window, text="B")
textB.grid(column=1, row=1)
txtInpB = Entry(window, width=15, textvariable=B)
txtInpB.grid(column=1, row=2)

textRes = Label(window, width=10, text="Результат: ")
textRes.grid(column=0, row=3)

btnPlus = Button(window, width=10, text="+", command=ClkPlus)
btnPlus.grid(column=0, row=6)

btnMinus = Button(window, width=10, text="-", command=ClkMinus)
btnMinus.grid(column=1, row=6)

btnDiv = Button(window, width=10, text="/", command=ClkDiv)
btnDiv.grid(column=2, row=6)

btnMult = Button(window, width=10, text="*", command=ClkMult)
btnMult.grid(column=3, row=6)






window.mainloop()