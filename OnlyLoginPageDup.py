from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import os

#from AfterLoginSingle import *
#from BeforeLoginSingle import *


def HomeLogin():
    '''load = Image.open('img.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        img.place(x=250, y=550)
        '''
    root = Tk()
    '''TopE.pack_forget()
    Bottom.pack_forget()'''
    root.title("Cab Booking System")
    root.geometry("1700x950+0+0")
    root.config(bg='black')
    frame = Frame(root, bg='black')
    frame.pack()

    username_verify = StringVar()
    password_verify = StringVar()
    varMsgDisplay = StringVar()

    lblTitle = Label(frame, text='Cab Booking System', font=('arial', 60, 'bold'), bg='black', fg='Cornsilk')
    lblTitle.grid(row=0, column=0, columnspan=2, pady=20)

    # Frame ================================================

    LoginFrame1 = LabelFrame(frame, width=1350, height=400, text="Login", fg='Cornsilk', font=('arial', 20, 'bold'), relief='ridge', bg='cadet blue', bd=40)
    LoginFrame1.grid(row=1, column=0)
    LoginFrame2 = LabelFrame(frame, width=1000, height=200, text="Log", fg='Cornsilk', font=('arial', 20, 'bold'), relief='ridge', bg='cadet blue', bd=40)
    LoginFrame2.grid(row=2, column=0)
    LoginFrame3 = LabelFrame(frame, width=500, height=100, fg='Cornsilk', font=('arial', 20, 'bold'), relief='sunken', bg='silver', bd=20)
    LoginFrame3.grid(row=3, column=0)

    msgDisplay = Label(LoginFrame3, font=('arial', 20, 'italic'), relief='sunken', textvariable=varMsgDisplay, width=56, height=3, bd=8, bg="silver", justify='center')
    msgDisplay.grid(row=6, column=1, columnspan=4)
    #-------------------------------------------------------------

    def login_sucess():
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)
        varMsgDisplay.set("Login Sucess !!")

    def password_not_recognised():
        password_entry1.delete(0, END)
        varMsgDisplay.set("Password Error")

    def user_not_found():
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)
        varMsgDisplay.set("User Not Found")

    def login_verify():

        username1 = username_verify.get()
        password1 = password_verify.get()

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                login_sucess()
                afterLogin()
            else:
                password_not_recognised()

        else:
            user_not_found()

        return

    def ireset():
        ireset = tkinter.messagebox.askyesno("Cab Login", "Confirm if you want to Reset")
        if ireset > 0:
            username_verify.set("")
            password_verify.set("")
            varMsgDisplay.set("")
            return

    def iExit():
        iExit = tkinter.messagebox.askyesno("Cab Login", "Confirm if you want to exit")
        if iExit > 0:
            root.destroy()
            return
    # textwidgets===========================================
    global username_entry1
    global password_entry1
    lblUsername = Label(LoginFrame1, text='Username', font=('arial', 30, 'bold'), bd=22, bg='cadet blue', fg='Cornsilk')
    lblUsername.grid(row=0, column=0)

    username_entry1 = Entry(LoginFrame1, text='Username', font=('arial', 30, 'bold'), bd=7, textvariable=username_verify, width=33)
    username_entry1.grid(row=0, column=1, padx=88)

    lblPassword = Label(LoginFrame1, text='Password', font=('arial', 30, 'bold'), bd=22, bg='cadet blue', fg='Cornsilk')
    lblPassword.grid(row=1, column=0)

    password_entry1 = Entry(LoginFrame1, text='Username', font=('arial', 30, 'bold'), show='*', bd=7, textvariable=password_verify, width=33)
    password_entry1.grid(row=1, column=1, columnspan=2, pady=30)
    # buttons===========================================
    btnLogin = Button(LoginFrame2, text='Login', width=15, font=('arial', 25, 'bold'), command=lambda: [login_verify()])
    btnLogin.grid(row=3, column=0, pady=20, padx=8)

    btnReg = Button(LoginFrame2, text='Register', width=15, font=('arial', 25, 'bold'))
    btnReg.grid(row=3, column=1, pady=20, padx=8)

    btnReset = Button(LoginFrame2, text='Reset', width=15, font=('arial', 25, 'bold'), command=ireset)
    btnReset.grid(row=3, column=2, pady=20, padx=8)

    btnExit = Button(LoginFrame2, text='Exit', width=15, font=('arial', 25, 'bold'), command=iExit)
    btnExit.grid(row=3, column=3, pady=20, padx=8)
    #=================================================

    #-------------------------------------------


HomeLogin()
