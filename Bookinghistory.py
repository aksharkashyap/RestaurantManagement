
from tkinter import *


def History():
    root = Tk()
    root.geometry("600x200")
    root.title("LPU Cab Booking System")
    root.configure(background='blue')
    #------------Frames--------------------------------------------
    Tops = Frame(root, width=600, height=50, bd=14, relief='raise')
    Tops.pack(side=TOP)

    lbl = Label(Tops, text="Booking Reference Number")
    lbl.grid(column=150, row=90)
    txt = Entry(Tops, width=10)
    txt.grid(column=151, row=90, padx=20)

    lbl1 = Label(Tops, text="Booking Date")
    lbl1.grid(column=150, row=91)
    txt1 = Entry(Tops, width=10)
    txt1.grid(column=151, row=91)

    btn1 = Button(Tops, text="Submit", bg="yellow")
    btn1.grid(column=151, row=92, pady=10)


History()
