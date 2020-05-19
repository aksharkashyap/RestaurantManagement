from tkinter import *
from tkinter import Tk
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry("1300x734+0+0")
root.configure(background='cadet blue')


def Routemap():

    root.geometry("1300x734+0+0")
    root.title("LPU Cab Booking System")
    load = Image.open('aashu.png')
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.pack()


btnCab = Button(root, text="Price List", bd=3, fg="red", font=('arial', 20, 'bold'), command=Routemap, height=2, width=12, bg="grey")
btnCab.place(x=2, y=6)
