from tkinter import *
from tkinter import Tk
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.configure(background='cadet blue')
root.geometry("1300x734")


def priceLst():

    root.title("LPU Cab Booking System")
    load = Image.open('Price List.png')
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.pack()


priceLst()
