from tkinter import*
from tkinter import Tk, StringVar, ttk, messagebox
import random
import time
import datetime
import os
from validate_email import validate_email  # For email verification


root = Tk()
root.geometry("1700x934+0+0")
root.title("LPU Cab Booking System")
root.configure(background='cadet blue')
#------------Frames--------------------------------------------
Tops = Frame(root, width=1350, height=900, bd=14, relief='raise')
Tops.pack(side=TOP)

Bottom = Frame(root, width=900, height=50, bd=8, relief='raise')
Bottom.pack(side=BOTTOM)

Bottom.configure(background='yellow')


#-----------Home functions--------------------------------------
def HomeExit():

    qExit = messagebox.askyesno("Quit system", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return


#...........................................................
Tops.configure(background='cadet blue')
lblTitle = Label(Tops, font=('arial', 40, 'bold'), text="Cab Booking System(LPU)", bd=10, width=30, height=2, justify='center', fg='black', bg='white')
lblTitle.grid(row=0, column=0)

lblcab = Label(Bottom, font=('arial', 25, 'bold'), text="Registration Link is Below", bd=10, width=50, height=2, justify='center', fg='black', bg='yellow')
lblcab.grid(row=1, column=0)
btnCab = Button(Bottom, text="Register Here", bd=3, fg="red", font=('arial', 20, 'bold'), height=2, width=12, bg="grey").grid(row=2, column=0)
btnCab = Button(Bottom, text="Register Here", bd=3, fg="red", font=('arial', 20, 'bold'), height=2, width=12, bg="grey").grid(row=2, column=0)

lblcab2 = Label(Bottom, font=('arial', 25, 'bold'), text="Looking for Login?", bd=10, width=50, height=2, justify='center', fg='black', bg='yellow')
lblcab2.grid(row=3, column=0)
btnCab2 = Button(Bottom, text="Login Here", bd=3, fg="red", font=('arial', 20, 'bold'), height=2, width=12, bg="grey").grid(row=4, column=0)

lblcab3 = Label(Bottom, font=('arial', 25, 'bold'), text="Price List is Here", bd=10, width=50, height=2, justify='center', fg='black', bg='yellow')
lblcab3.grid(row=5, column=0)
btnCab3 = Button(Bottom, text="Price List", bd=3, fg="red", font=('arial', 20, 'bold'), height=2, width=12, bg="grey").grid(row=6, column=0)

lblcab4 = Label(Bottom, font=('arial', 25, 'bold'), text="Booked Ticket History", bd=10, width=50, height=2, justify='center', fg='black', bg='yellow')
lblcab4.grid(row=7, column=0)
btnCab4 = Button(Bottom, text="History", bd=3, fg="red", font=('arial', 20, 'bold'), height=2, width=12, bg="grey").grid(row=8, column=0)

lblRoutemap = Label(Bottom, font=('arial', 25, 'bold'), text="Route Map", bd=10, width=50, height=2, justify='center', fg='black', bg='yellow')
lblRoutemap.grid(row=9, column=0)
btnRoutemap = Button(Bottom, text="Click Here", bd=3, fg="red", font=('arial', 20, 'bold'), height=2, width=12, bg="grey").grid(row=10, column=0)

lblcancel = Label(Bottom, font=('arial', 25, 'bold'), text="Cancel Booking", bd=10, width=50, height=2, justify='center', fg='black', bg='yellow')
lblcancel.grid(row=11, column=0)
btnCancel = Button(Bottom, text="Cancel", bd=3, fg="red", font=('arial', 20, 'bold'), height=2, width=12, bg="grey").grid(row=12, column=0)
btnExit = Button(Bottom, text="Exit", bd=3, fg="red", font=('arial', 20, 'bold'), height=2, width=12, bg="grey", command=HomeExit).grid(row=12, column=2)
