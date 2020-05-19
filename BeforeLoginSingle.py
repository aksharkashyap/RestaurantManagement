from tkinter import*
from tkinter import Tk, StringVar, ttk, messagebox
import os
from validate_email import validate_email  # For email verification
import random
import time
import datetime


def beforeLogin():
    root = Tk()
    # root.geometry("1075x850+0+0")
    height = 850
    width = 1075

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2)

    root.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))
    root.title("LPU Cab Booking System")
    root.configure(background='cadet blue')
    #------------Frames--------------------------------------------
    Tops = Frame(root, width=1350, height=900, bd=14, relief='raise')
    Tops.pack(side=TOP)

    f1 = Frame(root, width=900, height=650, bd=8, relief='raise')
    f1.pack(side=LEFT)
    f2 = Frame(root, width=440, height=650, bd=8, relief='raise')
    f2.pack(side=RIGHT)

    #-----------------Right Frame---------------------------------------
    frametopRight = Frame(f2, width=440, height=50, bd=12, relief='raise')
    frametopRight.pack(side=TOP)
    frameBottomRight = Frame(f2, width=440, height=200, bd=16, relief='raise')
    frameBottomRight.pack(side=BOTTOM)
    frameBottomRight2 = Frame(f2, height=20, bd=10, width=450, relief='sunken')
    frameBottomRight2.pack(side=BOTTOM)
    frameBottomRight3 = Frame(f2, width=450, height=500, bd=16, relief='raise')
    frameBottomRight3.pack(side=BOTTOM)
    #----------------------------------------------------------------------

    f1a = Frame(f1, width=900, height=600, bd=8, relief='raise')
    f1a.pack(side=TOP)

    frameLeftBottom = Frame(f1, width=900, height=490, bd=16, relief='raise')
    frameLeftBottom.pack(side=BOTTOM)

    topLeft1 = Frame(f1a, width=900, height=100, bd=16, relief='raise')
    topLeft1.pack(side=LEFT)
    '''topLeft2 = Frame(f1a, width=300, height=200, bd=16, relief='raise')
    topLeft2.pack(side=RIGHT)
    topLeft3 = Frame(f1a, width=300, height=200, bd=16, relief='raise')
    topLeft3.pack(side=RIGHT)
    '''

    #...........................................................
    Tops.configure(background='cadet blue')
    f1.configure(background='cadet blue')
    f2.configure(background='cadet blue')
    lblTitle = Label(Tops, font=('arial', 40, 'bold'), text="Cab Booking System(LPU)", bd=10, width=44, height=2, justify='center', fg='gold', bg='green')
    lblTitle.grid(row=0, column=0)

    lblTopRightTitle = Label(frametopRight, font=('arial', 24, 'bold'), text="LOGIN", bd=16, width=30, height=2, justify='center', fg='black', bg='tan3')
    lblTopRightTitle.grid(row=0, column=0)

    lblTopLeft = Label(topLeft1, font=('arial', 24, 'bold'), text="REGISTRATION", bd=10, width=35, height=2, justify='center', fg='black', bg='tan3')
    lblTopLeft.grid(row=0, column=0)

    #--------------Variable Login-------

    Username = StringVar()
    Password = StringVar()
    varMsgDisplay = StringVar()
    varMsgDisplay2 = StringVar()
    username_verify = StringVar()
    password_verify = StringVar()
    email_verify = StringVar()

    #-------Variable Registartion-------------
    username = StringVar()
    password = StringVar()
    confirmPassword = StringVar()
    FirstName = StringVar()
    LastName = StringVar()
    Age = StringVar()
    Email = StringVar()
    Mobile = StringVar()

    #-------------------BEFORE LOGIN - -------------------------------------------------------------
    #-------------------Registration & Login -----------------------------------------------------

    def exit():

        qExit = messagebox.askyesno("Quit system", "Do you want to quit?")
        if qExit > 0:
            root.destroy()
            return

    def ResetLogin():
        qExit = messagebox.askyesno("Reset", "Do you want to Reset?")
        if qExit > 0:
            username_verify.set("")
            password_verify.set("")
            varMsgDisplay.set("")
            return

    def ResetRegistration():
        qExit = messagebox.askyesno("Reset", "Do you want to Reset?")
        if qExit > 0:
            username.set("")
            password.set("")
            confirmPassword.set("")
            FirstName.set("")
            LastName.set("")
            Age.set("")
            Email.set("")
            Mobile.set("")
            varMsgDisplay2.set("")
            return

    def error():

        varMsgDisplay2.set("All Fields required !!")

    def error_passmatch():

        varMsgDisplay2.set("Password did not match !!")

    def error_len_mobile():

        varMsgDisplay2.set("Mobile Number Invalid !!")

    def error_age():

        varMsgDisplay2.set("Please Enter Valid Age !!")

    def error_passLen():
        varMsgDisplay2.set("Password length must be > 6")

    def error_passLen2():
        varMsgDisplay2.set("Password length must be < 10")

    def reg_success():

        varMsgDisplay2.set("Registration Sucess !!")

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

    def userExists():

        username1 = username_entry.get()

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if username1 in verify:
                userTaken()

        else:
            regDone()

    def userTaken():
        '''
        global screen9
        screen9 = Toplevel(screen)
        screen9.title("warning!")
        screen9.geometry("450x100")
        Label(screen9, text="User Already Exists! Please Try Different Username").pack()
        Button(screen9, text="OK", command=delete9).pack()'''
        varMsgDisplay2.set("User Already Exists! Please Try Different Username")

    def regDone():

        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info + "\n")
        file.write(firstName_info + "\n")
        file.write(lastName_info + "\n")
        file.write(age_info + "\n")
        file.write(mobile_info + "\n")
        file.write(email_info)
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        confirmPassword_entry.delete(0, END)
        FirstName_entry.delete(0, END)
        LastName_entry.delete(0, END)
        Age_entry.delete(0, END)
        Mobile_entry.delete(0, END)
        Email_entry.delete(0, END)

        '''Label(screen1, text="Processing...", fg="green", font=("calibri", 11)).place(x=590, y=660)'''
        reg_success()

    def login():

        global username_entry1
        global password_entry1

        lblUsername = Label(frameBottomRight3, text='Username', font=('arial', 20, 'bold'), width=13, bd=10, bg='cadet blue', fg='Cornsilk')
        lblUsername.grid(row=1, column=0)

        username_entry1 = Entry(frameBottomRight3, text='Username', font=('arial', 20, 'bold'), bd=10, textvariable=username_verify)
        username_entry1.grid(row=1, column=1)

        # space===========================================
        lblspace2 = Label(frameBottomRight3, font=('arial', 25, 'bold'), height=1)
        lblspace2.grid(row=2, column=0)

        #-------------------------------------------------
        lblPassword = Label(frameBottomRight3, text='Password', font=('arial', 20, 'bold'), width=13, bd=10, bg='cadet blue', fg='Cornsilk')
        lblPassword.grid(row=3, column=0)

        password_entry1 = Entry(frameBottomRight3, text='Username', font=('arial', 20, 'bold'), show='*', bd=10, textvariable=password_verify)
        password_entry1.grid(row=3, column=1)

        # space===========================================
        lblspace = Label(frameBottomRight2, font=('arial', 25, 'bold'), height=2, width=5)
        lblspace.grid(row=4, column=0)
        #-------------------------buttons
        btnLogin = Button(frameBottomRight2, text='Login', font=('arial', 25, 'bold'), height=2, width=7, command=login_verify)
        btnLogin.grid(row=4, column=0)

        btnReset = Button(frameBottomRight2, text='Reset', font=('arial', 25, 'bold'), height=2, width=7, command=ResetLogin)
        btnReset.grid(row=4, column=1)

        btnExit = Button(frameBottomRight2, text='Exit', font=('arial', 25, 'bold'), height=2, width=7, command=exit)
        btnExit.grid(row=4, column=2)

        msgDisplay = Label(frameBottomRight, font=('arial', 20, 'italic'), relief='sunken', textvariable=varMsgDisplay, width=36, height=12, bd=8, bg="silver", justify='center')
        msgDisplay.grid(row=5, column=1, columnspan=4)

    login()

    def register_user():
        global email_info
        global mobile_info
        global confirmPassword_info
        global firstName_info
        global lastName_info
        global age_info
        global username_info
        global password_info
        username_info = username.get()
        password_info = password.get()
        confirmPassword_info = confirmPassword.get()
        firstName_info = FirstName.get()
        lastName_info = LastName.get()
        age_info = Age.get()
        mobile_info = Mobile.get()
        email_info = Email.get()
        is_valid = validate_email(email_info)
        alphaCheckFirstName = firstName_info.isalpha()
        alphaCheckLastName = lastName_info.isalpha()
        numericCheckMob = mobile_info.isnumeric()

        if username_info == "":
            error()
        elif password_info == "":
            error()
        elif len(password_info) < 6:
            error_passLen()
        elif len(password_info) > 10:
            error_passLen2()
        elif confirmPassword_info == "":
            error()
        elif password_info != confirmPassword_info:
            error_passmatch()
        elif firstName_info == "":
            error()
        elif alphaCheckFirstName == False:
            varMsgDisplay2.set("Use characters only")
        elif len(firstName_info) < 3:
            varMsgDisplay2.set("First Name length should be >= 3 ")
        elif lastName_info == "":
            error()
        elif alphaCheckLastName == False:
            varMsgDisplay2.set("Use characters only")
        elif len(firstName_info) < 3:
            varMsgDisplay2.set("Last Name length should be >= 3 ")
        elif firstName_info == lastName_info:
            varMsgDisplay2.set("First Name & Last Name must be Different")
        elif age_info == "":
            error()
        elif (age_info) == "0":
            error_age()
        elif len(age_info) > 2:
            error_age()
        #-----------------------email verification-------------
        elif is_valid == False:
            varMsgDisplay2.set("Invalid Email")

        elif email_info == "":
            error()
        #--------------------------------------------------
        elif mobile_info == "":
            error()
        elif numericCheckMob == False:
            varMsgDisplay2.set("Invalid Mobile Number")
        elif len(mobile_info) > 10 or len(mobile_info) < 10:
            error_len_mobile()

        else:
            userExists()

    def register():
        #----------------For Single Module(Without HomeRegLoginBoth Function)
        '''global username
        global password
        global FirstName
        global LastName
        global Mobile
        global Age
        global Email
        global confirmPassword'''
        #-------------------------------------------------------------
        global confirmPassword_entry
        global username_entry
        global password_entry
        global FirstName_entry
        global LastName_entry
        global Age_entry
        global Email_entry
        global Mobile_entry
        lblRegUserName = Label(frameLeftBottom, text='Username', font=('arial', 20, 'bold'), width=15, bd=10, bg='cadet blue', fg='Cornsilk')
        lblRegUserName.grid(row=2, column=0)
        username_entry = Entry(frameLeftBottom, font=('arial', 20, 'bold'), width=25, bd=10, textvariable=username)
        username_entry.grid(row=2, column=1)

        lblRegUserPass = Label(frameLeftBottom, text='Password', font=('arial', 20, 'bold'), width=15, bd=10, bg='cadet blue', fg='Cornsilk')
        lblRegUserPass.grid(row=3, column=0)
        password_entry = Entry(frameLeftBottom, width=25, font=('arial', 20, 'bold'), show='*', bd=10, textvariable=password)
        password_entry.grid(row=3, column=1)

        lblRegConfirmPass = Label(frameLeftBottom, text='Confirm Password', font=('arial', 20, 'bold'), width=15, bd=10, bg='cadet blue', fg='Cornsilk')
        lblRegConfirmPass.grid(row=4, column=0)
        confirmPassword_entry = Entry(frameLeftBottom, width=25, font=('arial', 20, 'bold'), show='*', bd=10, textvariable=confirmPassword)
        confirmPassword_entry.grid(row=4, column=1)

        lblRegFristName = Label(frameLeftBottom, text='First Name', font=('arial', 20, 'bold'), width=15, bd=10, bg='cadet blue', fg='Cornsilk')
        lblRegFristName.grid(row=5, column=0)
        FirstName_entry = Entry(frameLeftBottom, width=25, font=('arial', 20, 'bold'), bd=10, textvariable=FirstName)
        FirstName_entry.grid(row=5, column=1)

        lblRegLastName = Label(frameLeftBottom, text='Last Name', font=('arial', 20, 'bold'), width=15, bd=10, bg='cadet blue', fg='Cornsilk')
        lblRegLastName.grid(row=6, column=0)
        LastName_entry = Entry(frameLeftBottom, width=25, font=('arial', 20, 'bold'), bd=10, textvariable=LastName)
        LastName_entry.grid(row=6, column=1)

        lblRegAge = Label(frameLeftBottom, text='Age', font=('arial', 20, 'bold'), width=15, bd=10, bg='cadet blue', fg='Cornsilk')
        lblRegAge.grid(row=7, column=0)
        Age_entry = Entry(frameLeftBottom, width=25, font=('arial', 20, 'bold'), bd=10, textvariable=Age)
        Age_entry.grid(row=7, column=1)

        lblRegEmail = Label(frameLeftBottom, text='Email', font=('arial', 20, 'bold'), bd=10, width=15, bg='cadet blue', fg='Cornsilk')
        lblRegEmail.grid(row=8, column=0)
        Email_entry = Entry(frameLeftBottom, width=25, font=('arial', 20, 'bold'), bd=10, textvariable=Email)
        Email_entry.grid(row=8, column=1)

        lblRegMobile = Label(frameLeftBottom, text='Mobile Number', font=('arial', 20, 'bold'), width=15, bd=10, bg='cadet blue', fg='Cornsilk')
        lblRegMobile.grid(row=9, column=0)

        Mobile_entry = Entry(frameLeftBottom, width=25, font=('arial', 20, 'bold'), bd=10, textvariable=Mobile)
        Mobile_entry.grid(row=9, column=1)

        btnReg = Button(frameLeftBottom, text="Register", bd=3, fg="red", font=('arial', 22, 'bold'), height=2, width=12, bg="grey", command=register_user).grid(row=10, column=0)

        btnReset = Button(frameLeftBottom, text="Reset", bd=3, fg="red", font=('arial', 22, 'bold'), width=12, height=2, bg="grey", command=ResetRegistration).grid(row=10, column=1)

        msgDisplay2 = Label(frameLeftBottom, font=('arial', 20, 'italic'), relief='sunken', width=42, height=2, textvariable=varMsgDisplay2, bd=8, bg="silver", justify='center')
        msgDisplay2.grid(row=11, column=0, columnspan=4)

    register()


beforeLogin()
