from tkinter import*
from tkinter import Tk, StringVar, ttk, messagebox
import os
from validate_email import validate_email# For email verification
import random
import time
import datetime



#-------------------------After Login(Booking System) ------------------
def afterLogin():
    #------------forget previous frames-----------------
    '''Tops.pack_forget()
    f1.pack_forget()
    f2.pack_forget()
    frametopRight.pack_forget()
    frameBottomRight.pack_forget()
    frameBottomRight2.pack_forget()
    frameBottomRight3.pack_forget()
    f1a.pack_forget()
    frameLeftBottom.pack_forget()
    topLeft1.pack_forget()'''

    #---------------------------------------------------
    root = Tk()
    #root.geometry("1538x714+0+0")
    height = 714
    width = 1538

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2)

    root.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))
    root.title("LPU Cab Booking System")
    root.configure(background='cadet blue')
    #------------Frames--------------------------------------------
    Topz = Frame(root, width=1350, height=900, bd=14, relief='raise')
    Topz.pack(side=TOP)

    f1r = Frame(root, width=900, height=650, bd=8, relief='raise')
    f1r.pack(side=LEFT)
    f2r = Frame(root, width=440, height=650, bd=8, relief='raise')
    f2r.pack(side=RIGHT)

    frameTopRightt = Frame(f2r, width=440, height=650, bd=12, relief='raise')
    frameTopRightt.pack(side=TOP)
    frameBottomRightt = Frame(f2r, width=440, height=50, bd=16, relief='raise')
    frameBottomRightt.pack(side=BOTTOM)

    f1aa = Frame(f1r, width=900, height=330, bd=8, relief='raise')
    f1aa.pack(side=TOP)
    f2aa = Frame(f1r, width=900, height=320, bd=6, relief='raise')
    f2aa.pack(side=BOTTOM)

    topLeftt1 = Frame(f1aa, width=300, height=200, bd=16, relief='raise')
    topLeftt1.pack(side=LEFT)
    topLeftt2 = Frame(f1aa, width=300, height=200, bd=16, relief='raise')
    topLeftt2.pack(side=RIGHT)
    topLeftt3 = Frame(f1aa, width=300, height=200, bd=16, relief='raise')
    topLeftt3.pack(side=RIGHT)

    #..........................................................
    bottomLeftt1 = Frame(f2aa, width=450, height=450, bd=14, relief='raise')
    bottomLeftt1.pack(side=LEFT)
    bottomLeftt2 = Frame(f2aa, width=450, height=450, bd=14, relief='raise')
    bottomLeftt2.pack(side=RIGHT)
    #...........................................................
    Topz.configure(background='cadet blue')
    f1r.configure(background='cadet blue')
    f2r.configure(background='cadet blue')
    lblTitle = Label(Topz, font=('arial', 40, 'bold'), text="Cab Booking System(LPU)", bd=10, width=50,height=2, justify='center',fg='gold',bg='green')
    lblTitle.grid(row=0, column=0)
    #--------Var declare-----------------------------------------
    global operator
    Date1 = StringVar()
    time1 = StringVar()
    CabType = StringVar()
    TicketPrice = StringVar()
    Child_Ticket = StringVar()
    Adult_Ticket = StringVar()
    From_Destination= StringVar()
    To_Destination= StringVar()
    Fee_Price= StringVar()
    Route = StringVar()
    Receipt_Ref = StringVar()
    var_result = StringVar()
    var_result2 = StringVar()
    CabType.set("")
    TicketPrice.set("")
    Child_Ticket.set("")
    Adult_Ticket.set("")
    From_Destination.set("")
    To_Destination.set("")
    Fee_Price.set("")
    Route.set("")
    Receipt_Ref.set("")

    #--------bg colours------
    '''
    OliveDrab1
    chocolate1
    '''
    #...........................................................
    lblReceipt = Label(frameTopRightt, font=('Times New Romen', 22, 'bold'), text="Cab Booking System",bg='chocolate1', width=39,height=3, justify='center')
    lblReceipt.grid(row=0, column=0)

    #..........................spacing.........................
    '''lblsp = Label(frameBottomRightt,font=('arial',14,'bold'),width=52,height=2,relief='sunken',background='silver',justify='center')
    lblsp.grid(row=2,column=0,columnspan=4)'''
    entResult2 = Label(frameBottomRightt, font=('arial', 20, 'italic'),relief='sunken',width=35,textvariable=var_result, bd=8, bg="silver", justify='center')
    entResult2.grid(row=0,column=0,columnspan=4)

    #................................................
    lblCabType1 = Label(frameBottomRightt, font=('arial', 14, 'bold'), text="Cab Type", width=16,bd=4, relief='sunken', justify='center')
    lblCabType1.grid(row=1, column=0)

    lblCabType2 = Label(frameBottomRightt, font=('arial', 14, 'bold'), width=16,bd=4, relief='sunken',textvariable=CabType, justify='center')
    lblCabType2.grid(row=2, column=0)


    lblTicket1 = Label(frameBottomRightt, font=('arial', 14, 'bold'), text="Ticket", width=8,bd=4,relief='sunken', justify='center')
    lblTicket1.grid(row=1, column=1)
    lblTicket2 = Label(frameBottomRightt, font=('arial', 14, 'bold'), width=8, relief='sunken',bd=4,textvariable=TicketPrice, justify='center')
    lblTicket2.grid(row=2, column=1)


    lblAdult1 = Label(frameBottomRightt, font=('arial', 14, 'bold'), text="Adult", width=8,bd=4, relief='sunken', justify='center')
    lblAdult1.grid(row=1, column=2)
    lblAdult2 = Label(frameBottomRightt, font=('arial', 14, 'bold'), width=8, relief='sunken',bd=4,textvariable=Adult_Ticket, justify='center')
    lblAdult2.grid(row=2, column=2)

    lblChild1 = Label(frameBottomRightt, font=('arial', 14, 'bold'), text="Child",bd=4, width=6, relief='sunken', justify='center')
    lblChild1.grid(row=1, column=3)
    lblChild2 = Label(frameBottomRightt, font=('arial', 14, 'bold'), width=6, bd=4,relief='sunken',textvariable=Child_Ticket, justify='center')
    lblChild2.grid(row=2, column=3)


    lblFrom1 = Label(frameBottomRightt, font=('arial', 14, 'bold'), text="From", width=16,bd=3, relief='sunken', justify='center')
    lblFrom1.grid(row=3, column=1)
    lblFrom2 = Label(frameBottomRightt, font=('arial', 14, 'bold'), width=16, relief='sunken',bd=3,textvariable=From_Destination, justify='center')
    lblFrom2.grid(row=3, column=2)


    lblTo1 = Label(frameBottomRightt, font=('arial', 14, 'bold'), text="To", width=16,bd=3, relief='sunken', justify='center')
    lblTo1.grid(row=4, column=1)
    lblTo2 = Label(frameBottomRightt, font=('arial', 14, 'bold'), width=16,bd=3, relief='sunken',textvariable=To_Destination, justify='center')
    lblTo2.grid(row=4, column=2)


    lblPrice1 = Label(frameBottomRightt, font=('arial', 14, 'bold'), text="Price", width=16,bd=3, relief='sunken', justify='center')
    lblPrice1.grid(row=5, column=1)
    lblPrice2 = Label(frameBottomRightt, font=('arial', 14, 'bold'), width=16, relief='sunken',bd=3,textvariable=Fee_Price, justify='center')
    lblPrice2.grid(row=5, column=2)
    #..........................spacing.........................
    '''lblResult = Label(frameBottomRightt,font=('arial',14,'bold'),text="",width=52,height=2,background='silver',relief='sunken',justify='center')
    lblResult.grid(row=6,column=0,columnspan=4)'''
    entResult = Label(frameBottomRightt, font=('arial', 20),relief='sunken',width=35,textvariable=var_result2, bd=8, bg="silver", justify='center')
    entResult.grid(row=6,column=0,columnspan=4)
    #................................................

    lblRefNo1 = Label(frameBottomRightt, font=('arial', 14, 'bold'), text="Ref No", width=16,height=2, relief='sunken', justify='center')
    lblRefNo1.grid(row=7, column=0)
    lblRefNo2 = Label(frameBottomRightt, font=('arial', 14, 'bold'), width=16,height=2, relief='sunken',textvariable=Receipt_Ref, justify='center')
    lblRefNo2.grid(row=8, column=0)

    lblTime1 = Label(frameBottomRightt, font=('arial', 14, 'bold'), text="Time", width=8,height=2, relief='sunken', justify='center')
    lblTime1.grid(row=7, column=1)
    lblTime2 = Label(frameBottomRightt, font=('arial', 14, 'bold'), width=8,height=2, relief='sunken', textvariable=time1, justify='center')
    lblTime2.grid(row=8, column=1)

    lblDate1 = Label(frameBottomRightt, font=('arial', 14, 'bold'), text="Date", width=8,height=2, relief='sunken', justify='center')
    lblDate1.grid(row=7, column=2)
    lblDate2 = Label(frameBottomRightt, font=('arial', 14, 'bold'), width=8, height=2,relief='sunken', textvariable=Date1, justify='center')
    lblDate2.grid(row=8, column=2)

    lblRoute1 = Label(frameBottomRightt, font=('arial', 14, 'bold'), text="Route", width=6,height=2, relief='sunken', justify='center')
    lblRoute1.grid(row=7, column=3)
    lblRoute2 = Label(frameBottomRightt, font=('arial', 14, 'bold'), width=6,height=2, relief='sunken',textvariable=Route, justify='center')
    lblRoute2.grid(row=8, column=3)

    #.....................Functions..................


    def btnClick(numbers):
        global operator
        operator = operator + str(numbers)
        text_Input.set(operator)


    def btnClearDisplay():
        global operator
        operator = ""
        text_Input.set("")


    def btnEqualsInput():
        global operator
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator = ""


    def iExit():
        qExit = messagebox.askyesno("Quit system", "Do you want to quit?")
        if qExit>0:
            root.destroy()
            return

    def booking_confirmation():
        if example.has_been_called:
            print("foo bar")


    def Travel_Cost_Adult_Calc_Standard():

            Tcost = float(50.8)
            Single = float(var12.get())
            Return = float(var6.get())
            Adult_Tax = "Rs", str('%.2f'%((Tcost * (Single+Return)*0.03)))
            Adult_Fees = "Rs", str('%.2f'%(Tcost * (Single+Return)))
            TotalCost = "Rs", str('%.2f'%((Tcost * (Single+Return)) +((Tcost * (Single+Return))*0.03)))
            Tax.set(Adult_Tax)
            SubTotal.set(Adult_Fees)
            CabType.set("Standard")
            TicketPrice.set(Adult_Fees)
            Child_Ticket.set("No")
            Adult_Ticket.set("Yes")
            Fee_Price.set(TotalCost)
            Total.set(TotalCost)
            var_result.set("Booking Details")
            var_result2.set("Click 'Book' To Confirm ")


    def Travel_Cost_Child_Calc_Standard():
            Tcost = float(33.8)
            Single = float(var12.get())
            Return = float(var6.get())
            Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
            Child_Fees = "Rs", str('%.2f'%(Tcost * (Single+Return)))
            TotalCost = "Rs", str('%.2f'%((Tcost * (Single+Return)) +(Tcost *0)))
            Tax.set(Child_Tax)
            SubTotal.set(Child_Fees)
            CabType.set("Standard")
            TicketPrice.set(Child_Fees)
            Child_Ticket.set("Yes")
            Adult_Ticket.set("No")

            Fee_Price.set(TotalCost)
            Total.set(TotalCost)
            var_result.set("Booking Details")
            var_result2.set("Click 'Book' To Confirm ")



    def Travel_Cost_Both_Calc_Standard():
            T_Child_Cost = float(33.8)
            T_Adult_cost = float(50.8)
            Single = float(var12.get())
            Return = float(var6.get())

            Child_Tax = ((T_Child_Cost * 0))
            Child_Fees = ((T_Child_Cost * (Single+Return)))
            Total_Child_Cost = ((T_Child_Cost * (Single+Return)) +(T_Child_Cost *0))

            Adult_Tax = ((T_Adult_cost * (Single+Return))*0.03)
            Adult_Fees = (T_Adult_cost * (Single+Return))
            Total_Adult_Cost = (((T_Adult_cost * (Single+Return)) +((T_Adult_cost * (Single+Return))*0.03)))
            totaltax = "Rs",str('%.2f'%(Adult_Tax+Child_Tax))
            totalfees = "Rs",str('%.2f'%(Adult_Fees+Child_Fees))
            totalprice = "Rs",str('%.2f'%(Total_Adult_Cost+Total_Child_Cost))

            tprice = "Rs", str('%.2f'%(T_Child_Cost + T_Adult_cost))

            Tax.set(totaltax)
            SubTotal.set(totalfees)
            CabType.set("Standard")
            TicketPrice.set(tprice)
            Child_Ticket.set("Yes")
            Adult_Ticket.set("Yes")

            Fee_Price.set(totalprice)
            Total.set(totalprice)
            var_result.set("Booking Details")
            var_result2.set("Click 'Book' To Confirm ")


    def Travel_Cost_Adult_Calc_Mini():
            Tcost = float(30.8)
            Single = float(var12.get())
            Return = float(var6.get())
            Adult_Tax = "Rs", str('%.2f'%((Tcost * (Single+Return)*0.03)))
            Adult_Fees = "Rs", str('%.2f'%(Tcost * (Single+Return)))
            TotalCost = "Rs", str('%.2f'%((Tcost * (Single+Return)) +((Tcost * (Single+Return))*0.03)))
            Tax.set(Adult_Tax)
            SubTotal.set(Adult_Fees)
            CabType.set("Mini")
            TicketPrice.set(Adult_Fees)
            Child_Ticket.set("No")
            Adult_Ticket.set("Yes")

            Fee_Price.set(TotalCost)
            Total.set(TotalCost)
            var_result.set("Booking Details")
            var_result2.set("Click 'Book' To Confirm ")


    def Travel_Cost_Child_Calc_Mini():
            Tcost = float(23.8)
            Single = float(var12.get())
            Return = float(var6.get())
            Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
            Child_Fees = "Rs", str('%.2f'%(Tcost * (Single+Return)))
            TotalCost = "Rs", str('%.2f'%((Tcost * (Single+Return)) +(Tcost *0)))
            Tax.set(Child_Tax)
            SubTotal.set(Child_Fees)
            CabType.set("Mini")
            TicketPrice.set(Child_Fees)
            Child_Ticket.set("Yes")
            Adult_Ticket.set("No")

            Fee_Price.set(TotalCost)
            Total.set(TotalCost)
            var_result.set("Booking Details")
            var_result2.set("Click 'Book' To Confirm ")


    def Travel_Cost_Both_Calc_Mini():
            T_Child_Cost = float(23.8)
            T_Adult_cost = float(30.8)
            Single = float(var12.get())
            Return = float(var6.get())
            Child_Tax = ((T_Child_Cost * 0))
            Child_Fees = ((T_Child_Cost * (Single+Return)))
            Total_Child_Cost = ((T_Child_Cost * (Single+Return)) +(T_Child_Cost *0))

            Adult_Tax = ((T_Adult_cost * (Single+Return))*0.03)
            Adult_Fees = (T_Adult_cost * (Single+Return))
            Total_Adult_Cost = (((T_Adult_cost * (Single+Return)) +((T_Adult_cost * (Single+Return))*0.03)))
            totaltax = "Rs",str('%.2f'%(Adult_Tax+Child_Tax))
            totalfees = "Rs",str('%.2f'%(Adult_Fees+Child_Fees))
            totalprice = "Rs",str('%.2f'%(Total_Adult_Cost+Total_Child_Cost))

            tprice = "Rs", str('%.2f'%(T_Child_Cost + T_Adult_cost))

            Tax.set(totaltax)
            SubTotal.set(totalfees)
            CabType.set("Mini")
            TicketPrice.set(tprice)
            Child_Ticket.set("Yes")
            Adult_Ticket.set("Yes")

            Fee_Price.set(totalprice)
            Total.set(totalprice)
            var_result.set("Booking Details")
            var_result2.set("Click 'Book' To Confirm ")


    def Travel_Cost_CampusTour_Adult():
            Tcost = float(100.8)
            Single = float(var12.get())
            Adult_Tax = "Rs", str('%.2f'%((Tcost * (Single)*0.03)))
            Adult_Fees = "Rs", str('%.2f'%(Tcost * (Single)))
            TotalCost = "Rs", str('%.2f'%((Tcost * (Single)) +((Tcost * (Single))*0.03)))
            Tax.set(Adult_Tax)
            SubTotal.set(Adult_Fees)
            CabType.set("Campus Tour")
            TicketPrice.set(Adult_Fees)
            Child_Ticket.set("No")
            Adult_Ticket.set("Yes")
            From_Destination.set("LPU MG")
            To_Destination.set("Campus")
            Fee_Price.set(TotalCost)
            Total.set(TotalCost)
            var_result.set("Booking Details")
            var_result2.set("Click 'Book' To Confirm ")

    def Travel_Cost_CampusTour_Child():
            Tcost = float(70.8)
            Single = float(var12.get())
            Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
            Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
            TotalCost = "Rs", str('%.2f'%((Tcost * Single) +(Tcost *0)))
            Tax.set(Child_Tax)
            SubTotal.set(Child_Fees)
            CabType.set("Campus Tour")
            TicketPrice.set(Child_Fees)
            Child_Ticket.set("Yes")
            Adult_Ticket.set("No")
            From_Destination.set("LPU MG")
            To_Destination.set("Campus")
            Fee_Price.set(TotalCost)
            Total.set(TotalCost)
            var_result.set("Booking Details")
            var_result2.set("Click 'Book' To Confirm ")

    def Travel_Cost_CampusTour_Both():

            T_Child_Cost = float(70.8)
            T_Adult_cost = float(100.8)
            Single = float(var12.get())

            Child_Tax = ((T_Child_Cost * 0))
            Child_Fees = ((T_Child_Cost * Single))
            Total_Child_Cost = ((T_Child_Cost * Single) +(T_Child_Cost *0))

            Adult_Tax = ((T_Adult_cost * Single)*0.03)
            Adult_Fees = (T_Adult_cost * Single)
            Total_Adult_Cost = (((T_Adult_cost * Single) +((T_Adult_cost * Single)*0.03)))
            totaltax = "Rs",str('%.2f'%(Adult_Tax+Child_Tax))
            totalfees = "Rs",str('%.2f'%(Adult_Fees+Child_Fees))
            totalprice = "Rs",str('%.2f'%(Total_Adult_Cost+Total_Child_Cost))

            tprice = "Rs", str('%.2f'%(T_Child_Cost + T_Adult_cost))

            Tax.set(totaltax)
            SubTotal.set(totalfees)
            CabType.set("Campus Tour")
            TicketPrice.set(tprice)
            Child_Ticket.set("Yes")
            Adult_Ticket.set("Yes")
            From_Destination.set("LPU MG")
            To_Destination.set("Campus")
            Fee_Price.set(totalprice)
            Total.set(totalprice)
            var_result.set("Booking Details")
            var_result2.set("Click 'Book' To Confirm ")


    def Booking_confirmation():
        qExit = messagebox.askyesno("Booking", "Do you want to book?")
        if qExit > 0:
            if Travel_Cost.has_been_called:
                if var_result.get()=="":
                    var_result2.set("Oops!!Fill the Required Details")
                else:
                    print("Booking Successful")
                    #----------------------------Date and Time-------------
                    Date1.set(time.strftime("%d/%m/%y"))
                    time1.set(time.strftime('%H:%M:%S'))
                    #------------------------------------------------------
                    var_result.set("Booking Details")
                    var_result2.set("Congrats! You Have Got A Ticket !!")
                    Route.set("Direct")
                    #---DISABLE THE TOTAL BUTTON AND REMARKS FIELD--------
                    btnTotal.config(state=DISABLED)
                    btnBook.config(state=DISABLED)
                    entRemarks.config(state=DISABLED)
                    entReturn.config(state=DISABLED)
                    entSingle.config(state=DISABLED)
                    #-----Transaction Referance Number---------------------
                    x=random.randint(109,5876)
                    randomRef = str(x)
                    Receipt_Ref.set("TFL" + randomRef)
            else:
                var_result2.set("Oops!!Fill the Required Details")
            return


    #-----------------------------------------Travel cost calculation --------------------------------------------------
    def Travel_Cost():
        Travel_Cost.has_been_called = True

        #----------------------Travel cost calculation -Main Gate  to Campus(Campus Tour)--------------------------------------------------
        if (var13.get() == 'Main Gate' and var9.get() == 'Campus Tour'  and var3.get() == 1 and var4.get() == 1 ):
            Travel_Cost_CampusTour_Adult()

        elif (var13.get() == 'Main Gate' and var9.get() =='Campus Tour'  and var3.get() ==1 and var5.get() ==1):
            Travel_Cost_CampusTour_Child()
        if (var13.get() == 'Main Gate' and var9.get() == 'Campus Tour'  and var3.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_CampusTour_Both()
        #----------------------Travel cost calculation -Main Gate  to Girls Hostel (standard)--------------------------------------------------

        if (var13.get() == 'Main Gate' and var9.get() == 'Girls Hostel'  and var1.get() == 1 and var4.get() == 1 ):
           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("GH")
        elif (var13.get() == 'Main Gate' and var9.get() == 'Girls Hostel'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("GH")
        if (var13.get() == 'Main Gate' and var9.get() == 'Girls Hostel'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("GH")
    #------------------Travel cost calculation -main gate to girls hostel(mini)-------------------------------------------------
        if (var13.get() == 'Main Gate' and var9.get() == 'Girls Hostel' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("LPU MG")
            To_Destination.set("GH")
        elif (var13.get() == 'Main Gate' and var9.get() == 'Girls Hostel'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("LPU MG")
            To_Destination.set("GH")
        if (var13.get() == 'Main Gate' and var9.get() == 'Girls Hostel' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Mini()
           From_Destination.set("LPU MG")
           To_Destination.set("GH")

    #----------------------Travel cost calculation -Girls Hostel TO Main Gate (standard)--------------------------------------------------

        if (var13.get() == 'Girls Hostel' and var9.get() == 'Main Gate'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Main Gate")

        elif (var13.get() == 'Girls Hostel' and var9.get() == 'Main Gate'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Main Gate")
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Main Gate'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Main Gate")
    #------------------Travel cost calculation -GIRLS HOSTEL to MAIN GATE (mini)-------------------------------------------------
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Main Gate' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Main Gate")
        elif (var13.get() == 'Girls Hostel' and var9.get() == 'Main Gate'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Main Gate")
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Main Gate' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Main Gate")

    #----------------------Travel cost calculation -Girls Hostel TO CSE Block (standard)--------------------------------------------------

        if (var13.get() == 'Girls Hostel' and var9.get() == 'CSE Block'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("CSE Block")

        elif (var13.get() == 'Girls Hostel' and var9.get() == 'CSE Block'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("CSE Block")
        if (var13.get() == 'Girls Hostel' and var9.get() == 'CSE Block'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("CSE Block")
    #------------------Travel cost calculation -GIRLS HOSTEL to CSE Block (mini)-------------------------------------------------
        if (var13.get() == 'Girls Hostel' and var9.get() == 'CSE Block' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("CSE Block")
        elif (var13.get() == 'Girls Hostel' and var9.get() == 'CSE Block'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("CSE Block")
        if (var13.get() == 'Girls Hostel' and var9.get() == 'CSE Block' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("CSE Block")

    #----------------------Travel cost calculation -Girls Hostel TO Uni Mall  (standard)--------------------------------------------------

        if (var13.get() == 'Girls Hostel' and var9.get() == 'Uni Mall'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Uni Mall")

        elif (var13.get() == 'Girls Hostel' and var9.get() == 'Uni Mall'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Uni Mall")
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Uni Mall'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Uni Mall")
    #------------------Travel cost calculation -GIRLS HOSTEL to Uni Mall (mini)-------------------------------------------------
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Uni Mall' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Uni Mall")
        elif (var13.get() == 'Girls Hostel' and var9.get() == 'Uni Mall'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Uni Mall")
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Uni Mall' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Uni Mall")

    #----------------------Travel cost calculation -Girls Hostel TO Uni Hospital  (standard)--------------------------------------------------

        if (var13.get() == 'Girls Hostel' and var9.get() == 'Uni Hospital'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Uni Hospital")

        elif (var13.get() == 'Girls Hostel' and var9.get() == 'Uni Hospital'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Uni Hospital")
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Uni Hospital'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Uni Hospital")
    #------------------Travel cost calculation -GIRLS HOSTEL to Uni Hospital (mini)-------------------------------------------------
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Uni Hospital' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Uni Hospital")
        elif (var13.get() == 'Girls Hostel' and var9.get() == 'Uni Hospital'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Uni Hospital")
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Uni Hospital' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Uni Hospital")

    #----------------------Travel cost calculation -Girls Hostel TO Mechanical Block  (standard)--------------------------------------------------

        if (var13.get() == 'Girls Hostel' and var9.get() == 'Mechanical Block '  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Mechanical Block ")

        elif (var13.get() == 'Girls Hostel' and var9.get() == 'Mechanical Block '  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Mechanical Block ")
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Mechanical Block '  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Mechanical Block ")
    #------------------Travel cost calculation -GIRLS HOSTEL to Mechanical Block (mini)-------------------------------------------------
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Mechanical Block ' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Mechanical Block ")
        elif (var13.get() == 'Girls Hostel' and var9.get() == 'Mechanical Block '  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Mechanical Block ")
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Mechanical Block ' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Mechanical Block ")

    #----------------------Travel cost calculation -Girls Hostel TO Boys Hostel  (standard)--------------------------------------------------

        if (var13.get() == 'Girls Hostel' and var9.get() == 'Boys Hostel '  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Boys Hostel ")

        elif (var13.get() == 'Girls Hostel' and var9.get() == 'Boys Hostel '  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Boys Hostel ")
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Boys Hostel '  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Boys Hostel ")
    #------------------Travel cost calculation -GIRLS HOSTEL to Mechanical Block (mini)-------------------------------------------------
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Boys Hostel ' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Boys Hostel ")
        elif (var13.get() == 'Girls Hostel' and var9.get() == 'Boys Hostel '  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Boys Hostel ")
        if (var13.get() == 'Girls Hostel' and var9.get() == 'Boys Hostel ' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Boys Hostel ")
    #--------------------------------'''

    #---------------------------------- Travel Cost Calculation Main Gate to Boys Hostel--------------
        if (var13.get() == 'Main Gate' and var9.get() == 'Boys Hostel'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("Boys Hostel")

        elif (var13.get() == 'Main Gate' and var9.get() == 'Boys Hostel'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("Boys Hostel")
        if (var13.get() == 'Main Gate' and var9.get() == 'Boys Hostel'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("Boys Hostel")
    #------------------Travel cost calculation -main gate to Boys Hostel(mini)-------------------------------------------------
        if (var13.get() == 'Main Gate' and var9.get() == 'Boys Hostel' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("LPU MG")
            To_Destination.set("Boys Hostel")
        elif (var13.get() == 'Main Gate' and var9.get() == 'Boys Hostel'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("LPU MG")
            To_Destination.set("Boys Hostel")
        if (var13.get() == 'Main Gate' and var9.get() == 'Boys Hostel' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Mini()
           From_Destination.set("LPU MG")
           To_Destination.set("Boys Hostel")

    #----------------------Travel cost calculation -Boys Hostel TO Main Gate (standard)--------------------------------------------------

        if (var13.get() == 'Boys Hostel' and var9.get() == 'Main Gate'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Main Gate")

        elif (var13.get() == 'Boys Hostel' and var9.get() == 'Main Gate'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Main Gate")
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Main Gate'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Main Gate")
    #------------------Travel cost calculation -Boys Hostel to MAIN GATE (mini)-------------------------------------------------
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Main Gate' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Main Gate")
        elif (var13.get() == 'Girls Hostel' and var9.get() == 'Main Gate'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Main Gate")
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Main Gate' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Main Gate")

    #----------------------Travel cost calculation -Boys Hostel TO CSE Block (standard)--------------------------------------------------

        if (var13.get() == 'Boys Hostel' and var9.get() == 'CSE Block'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("CSE Block")

        elif (var13.get() == 'Boys Hostel' and var9.get() == 'CSE Block'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("CSE Block")
        if (var13.get() == 'Boys Hostel' and var9.get() == 'CSE Block'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("CSE Block")
    #------------------Travel cost calculation -Boys Hostel to CSE Block (mini)-------------------------------------------------
        if (var13.get() == 'Boys Hostel' and var9.get() == 'CSE Block' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("CSE Block")
        elif (var13.get() == 'Boys Hostel' and var9.get() == 'CSE Block'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("CSE Block")
        if (var13.get() == 'Boys Hostel' and var9.get() == 'CSE Block' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("CSE Block")

    #----------------------Travel cost calculation -Boys Hostel TO Uni Mall  (standard)--------------------------------------------------

        if (var13.get() == 'Boys Hostel' and var9.get() == 'Uni Mall'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Uni Mall")

        elif (var13.get() == 'Boys Hostel' and var9.get() == 'Uni Mall'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Uni Mall")
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Uni Mall'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Uni Mall")
    #------------------Travel cost calculation -Boys Hostel to Uni Mall (mini)-------------------------------------------------
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Uni Mall' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Uni Mall")
        elif (var13.get() == 'Boys Hostel' and var9.get() == 'Uni Mall'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Uni Mall")
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Uni Mall' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Uni Mall")

    #----------------------Travel cost calculation -Boys Hostel TO Uni Hospital  (standard)--------------------------------------------------

        if (var13.get() == 'Boys Hostel' and var9.get() == 'Uni Hospital'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Uni Hospital")

        elif (var13.get() == 'Boys Hostel' and var9.get() == 'Uni Hospital'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Uni Hospital")
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Uni Hospital'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Uni Hospital")
    #------------------Travel cost calculation -Boys Hostel to Uni Hospital (mini)-------------------------------------------------
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Uni Hospital' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Uni Hospital")
        elif (var13.get() == 'Boys Hostel' and var9.get() == 'Uni Hospital'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Uni Hospital")
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Uni Hospital' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Uni Hospital")

    #----------------------Travel cost calculation -Boys Hostel TO Mechanical Block  (standard)--------------------------------------------------

        if (var13.get() == 'Girls Hostel' and var9.get() == 'Mechanical Block'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Mechanical Block ")

        elif (var13.get() == 'Girls Hostel' and var9.get() == 'Mechanical Block'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("Mechanical Block ")
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Mechanical Block'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Mechanical Block ")
    #------------------Travel cost calculation -Boys Hostel to Mechanical Block (mini)-------------------------------------------------
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Mechanical Block' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Mechanical Block ")
        elif (var13.get() == 'Boys Hostel' and var9.get() == 'Mechanical Block'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Mechanical Block ")
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Mechanical Block' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Mechanical Block ")

    #----------------------Travel cost calculation -Boys Hostel TO Girls Hostel  (standard)--------------------------------------------------

        if (var13.get() == 'Boys Hostel' and var9.get() == 'Girls Hostel'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Girls Hostel ")

        elif (var13.get() == 'Boys Hostel' and var9.get() == 'Girls Hostel '  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Girls Hostel ")
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Girls Hostel '  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Boys Hostel")
           To_Destination.set("Girls Hostel ")
    #------------------Travel cost calculation -Boys Hostel to Girls Hostel(mini)-------------------------------------------------
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Girls Hostel ' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Girls Hostel ")
        elif (var13.get() == 'Boys Hostel' and var9.get() == 'Girls Hostel '  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Girls Hostel ")
        if (var13.get() == 'Boys Hostel' and var9.get() == 'Girls Hostel ' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Boys Hostel")
            To_Destination.set("Girls Hostel ")

    #------------------Travel cost calculation - main gate to cse block(mini)-------------------------------------------------
        if (var13.get() == 'Main Gate' and var9.get() == 'CSE Block'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("CSE Block")

        elif (var13.get() == 'Main Gate' and var9.get() == 'CSE Block'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("CSE Block")
        if (var13.get() == 'Main Gate' and var9.get() == 'CSE Block'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("CSE Block")
    #------------------Travel cost calculation -main gate to CSE Block(mini)-------------------------------------------------
        if (var13.get() == 'Main Gate' and var9.get() == 'CSE Block' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("LPU MG")
            To_Destination.set("CSE Block")
        elif (var13.get() == 'Main Gate' and var9.get() == 'CSE Block'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("LPU MG")
            To_Destination.set("CSE Block")
        if (var13.get() == 'Main Gate' and var9.get() == 'CSE Block' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Mini()
           From_Destination.set("LPU MG")
           To_Destination.set("CSE Block")

    #----------------------Travel cost calculation - CSE Block TO Main Gate (standard)--------------------------------------------------

        if (var13.get() == 'CSE Block' and var9.get() == 'Main Gate'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Main Gate")

        elif (var13.get() == 'CSE Block' and var9.get() == 'Main Gate'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Main Gate")
        if (var13.get() == 'CSE Block' and var9.get() == 'Main Gate'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Main Gate")
    #------------------Travel cost calculation -CSE Block to MAIN GATE (mini)-------------------------------------------------
        if (var13.get() == 'CSE Block' and var9.get() == 'Main Gate' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Main Gate")
        elif (var13.get() == 'CSE Block' and var9.get() == 'Main Gate'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Main Gate")
        if (var13.get() == 'CSE Block' and var9.get() == 'Main Gate' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Main Gate")

    #----------------------Travel cost calculation - CSE Block TO Girls Hostel (standard)--------------------------------------------------

        if (var13.get() == 'CSE Block' and var9.get() == 'Girls Hostel'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Girls Hostel")

        elif (var13.get() == 'CSE Block' and var9.get() == 'Girls Hostel'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Girls Hostel")
        if (var13.get() == 'CSE Block' and var9.get() == 'Girls Hostel'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Girls Hostel")
    #------------------Travel cost calculation -CSE Block to Girls Hostel (mini)-------------------------------------------------
        if (var13.get() == 'CSE Block' and var9.get() == 'Girls Hostel' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Girls Hostel")
        elif (var13.get() == 'CSE Block' and var9.get() == 'Girls Hostel'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Girls Hostel")
        if (var13.get() == 'CSE Block' and var9.get() == 'Girls Hostel' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Girls Hostel")


    #----------------------Travel cost calculation -CSE Block TO Uni Mall  (standard)--------------------------------------------------

        if (var13.get() == 'CSE Block' and var9.get() == 'Uni Mall'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Uni Mall")

        elif (var13.get() == 'CSE Block' and var9.get() == 'Uni Mall'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Uni Mall")
        if (var13.get() == 'CSE Block' and var9.get() == 'Uni Mall'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Uni Mall")
    #------------------Travel cost calculation -CSE Block to Uni Mall (mini)-------------------------------------------------
        if (var13.get() == 'CSE Block' and var9.get() == 'Uni Mall' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Uni Mall")
        elif (var13.get() == 'CSE Block' and var9.get() == 'Uni Mall'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Uni Mall")
        if (var13.get() == 'CSE Block' and var9.get() == 'Uni Mall' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Uni Mall")

    #----------------------Travel cost calculation -CSE Block TO Uni Hospital  (standard)--------------------------------------------------

        if (var13.get() == 'CSE Block' and var9.get() == 'Uni Hospital'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Uni Hospital")

        elif (var13.get() == 'CSE Block' and var9.get() == 'Uni Hospital'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Uni Hospital")
        if (var13.get() == 'CSE Block' and var9.get() == 'Uni Hospital'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Uni Hospital")
    #------------------Travel cost calculation -CSE Block to Uni Hospital (mini)-------------------------------------------------
        if (var13.get() == 'CSE Block' and var9.get() == 'Uni Hospital' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Uni Hospital")
        elif (var13.get() == 'CSE Block' and var9.get() == 'Uni Hospital'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Uni Hospital")
        if (var13.get() == 'CSE Block' and var9.get() == 'Uni Hospital' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Uni Hospital")

    #----------------------Travel cost calculation -CSE Block TO Mechanical Block  (standard)--------------------------------------------------

        if (var13.get() == 'CSE Block' and var9.get() == 'Mechanical Block'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Mechanical Block ")

        elif (var13.get() == 'CSE Block' and var9.get() == 'Mechanical Block'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Mechanical Block ")
        if (var13.get() == 'CSE Block' and var9.get() == 'Mechanical Block'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Mechanical Block ")
    #------------------Travel cost calculation -CSE Block to Mechanical Block (mini)-------------------------------------------------
        if (var13.get() == 'CSE Block' and var9.get() == 'Mechanical Block' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Mechanical Block ")
        elif (var13.get() == 'CSE Block' and var9.get() == 'Mechanical Block'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Mechanical Block ")
        if (var13.get() == 'CSE Block' and var9.get() == 'Mechanical Block' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Mechanical Block ")

    #----------------------Travel cost calculation - CSE Block TO Boys Hostel  (standard)--------------------------------------------------

        if (var13.get() == 'CSE Block' and var9.get() == 'Boys Hostel'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Boys Hostel ")

        elif (var13.get() == 'CSE Block' and var9.get() == 'Boys Hostel'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Girls Hostel")
           To_Destination.set("CSE Block ")
        if (var13.get() == 'CSE Block' and var9.get() == 'Boys Hostel'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("CSE Block")
           To_Destination.set("Boys Hostel ")
    #------------------Travel cost calculation -CSE Block to Mechanical Block (mini)-------------------------------------------------
        if (var13.get() == 'CSE Block' and var9.get() == 'Boys Hostel' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("CSE Block")
            To_Destination.set("Boys Hostel ")
        elif (var13.get() == 'CSE Block' and var9.get() == 'Boys Hostel'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Boys Hostel ")
        if (var13.get() == 'CSE Block' and var9.get() == 'Boys Hostel' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Girls Hostel")
            To_Destination.set("Boys Hostel ")

    #------------------------------Main Gate To Mechanical Block-------------
        if (var13.get() == 'Main Gate' and var9.get() == 'Mechanical Block'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("LPU MG")

        elif (var13.get() == 'Main Gate' and var9.get() == 'Mechanical Block'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("Mechanical Block")
        if (var13.get() == 'Main Gate' and var9.get() == 'Mechanical Block'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("Mechanical Block")
    #------------------Travel cost calculation -main gate to Mechanical Block(mini)-------------------------------------------------
        if (var13.get() == 'Main Gate' and var9.get() == 'Mechanical Block' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("LPU MG")
            To_Destination.set("Mechanical Block")
        elif (var13.get() == 'Main Gate' and var9.get() == 'Mechanical Block'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("LPU MG")
            To_Destination.set("Mechanical Block")
        if (var13.get() == 'Main Gate' and var9.get() == 'Mechanical Block' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Mini()
           From_Destination.set("LPU MG")
           To_Destination.set("Mechanical Block")

    #----------------------Travel cost calculation -Mechanical Block TO Main Gate (standard)--------------------------------------------------

        if (var13.get() == 'Mechanical Block' and var9.get() == 'Main Gate'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Main Gate")

        elif (var13.get() == 'Mechanical Block' and var9.get() == 'Main Gate'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Main Gate")
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Main Gate'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Main Gate")
    #------------------Travel cost calculation -Mechanical Block to MAIN GATE (mini)-------------------------------------------------
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Main Gate' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Main Gate")
        elif (var13.get() == 'Mechanical Block' and var9.get() == 'Main Gate'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Main Gate")
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Main Gate' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Main Gate")

    #----------------------Travel cost calculation -Mechanical Block TO CSE Block (standard)--------------------------------------------------

        if (var13.get() == 'Mechanical Block' and var9.get() == 'CSE Block'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("CSE Block")

        elif (var13.get() == 'Mechanical Block' and var9.get() == 'CSE Block'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("CSE Block")
        if (var13.get() == 'Mechanical Block' and var9.get() == 'CSE Block'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("CSE Block")
    #------------------Travel cost calculation -Mechanical Block to CSE Block (mini)-------------------------------------------------
        if (var13.get() == 'Mechanical Block' and var9.get() == 'CSE Block' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("CSE Block")
        elif (var13.get() == 'Mechanical Block' and var9.get() == 'CSE Block'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("CSE Block")
        if (var13.get() == 'Mechanical Block' and var9.get() == 'CSE Block' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("CSE Block")

    #----------------------Travel cost calculation -Mechanical Block TO Uni Mall  (standard)--------------------------------------------------

        if (var13.get() == 'Mechanical Block' and var9.get() == 'Uni Mall'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Uni Mall")

        elif (var13.get() == 'Mechanical Block' and var9.get() == 'Uni Mall'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Uni Mall")
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Uni Mall'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Uni Mall")
    #------------------Travel cost calculation -Mechanical Block to Uni Mall (mini)-------------------------------------------------
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Uni Mall' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Uni Mall")
        elif (var13.get() == 'Mechanical Block' and var9.get() == 'Uni Mall'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Uni Mall")
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Uni Mall' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Uni Mall")

    #----------------------Travel cost calculation -Mechanical Block TO Uni Hospital  (standard)--------------------------------------------------

        if (var13.get() == 'Mechanical Block' and var9.get() == 'Uni Hospital'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Uni Hospital")

        elif (var13.get() == 'Mechanical Block' and var9.get() == 'Uni Hospital'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Uni Hospital")
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Uni Hospital'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Uni Hospital")
    #------------------Travel cost calculation -Mechanical Block to Uni Hospital (mini)-------------------------------------------------
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Uni Hospital' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Uni Hospital")
        elif (var13.get() == 'Mechanical Block' and var9.get() == 'Uni Hospital'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Uni Hospital")
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Uni Hospital' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Uni Hospital")

    #----------------------Travel cost calculation -Mechanical Block TO Girls Hostel  (standard)------------------------------

        if (var13.get() == 'Mechanical Block' and var9.get() == 'Girls Hostel'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Girls Hostel")

        elif (var13.get() == 'Mechanical Block' and var9.get() == 'Girls Hostel'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Girls Hostel")
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Girls Hostel'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Girls Hostel")
    #------------------Travel cost calculation -Mechanical Block to Girls Hostel (mini)-------------------------------------------------
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Girls Hostel ' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Girls Hostel")
        elif (var13.get() == 'Mechanical Block' and var9.get() == 'Girls Hostel'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Girls Hostel")
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Girls Hostel' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Girls Hostel")

    #----------------------Travel cost calculation -Mechanical Block TO Boys Hostel  (standard)--------------------------------------------------

        if (var13.get() == 'Mechanical Block' and var9.get() == 'Boys Hostel'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Boys Hostel ")

        elif (var13.get() == 'Mechanical Block' and var9.get() == 'Boys Hostel'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Boys Hostel ")
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Boys Hostel'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Mechanical Block")
           To_Destination.set("Boys Hostel ")
    #------------------Travel cost calculation -Mechanical Block to Mechanical Block (mini)-------------------------------------------------
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Boys Hostel' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Boys Hostel ")
        elif (var13.get() == 'Mechanical Block' and var9.get() == 'Boys Hostel'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Boys Hostel ")
        if (var13.get() == 'Mechanical Block' and var9.get() == 'Boys Hostel' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Mechanical Block")
            To_Destination.set("Boys Hostel ")
    #------------------------------Calculation - main gate to uni hospital----------------------

        if (var13.get() == 'Main Gate' and var9.get() == 'Uni Hospital'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("Uni Hospital")

        elif (var13.get() == 'Main Gate' and var9.get() == 'Uni Hospital'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("Uni Hospital")
        if (var13.get() == 'Main Gate' and var9.get() == 'Uni Hospital'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("Uni Hospital")
    #------------------Travel cost calculation -main gate to Uni Hospital(mini)-------------------------------------------------
        if (var13.get() == 'Main Gate' and var9.get() == 'Uni Hospital' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("LPU MG")
            To_Destination.set("Uni Hospital")
        elif (var13.get() == 'Main Gate' and var9.get() == 'Uni Hospital'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("LPU MG")
            To_Destination.set("Uni Hospital")
        if (var13.get() == 'Main Gate' and var9.get() == 'Uni Hospital' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Mini()
           From_Destination.set("LPU MG")
           To_Destination.set("Uni Hospital")

    #----------------------Travel cost calculation -Uni Hospital TO Main Gate (standard)--------------------------------------------------

        if (var13.get() == 'Uni Hospital' and var9.get() == 'Main Gate'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Main Gate")

        elif (var13.get() == 'Uni Hospital' and var9.get() == 'Main Gate'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Main Gate")
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Main Gate'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Main Gate")
    #------------------Travel cost calculation -Uni Hospital to MAIN GATE (mini)-------------------------------------------------
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Main Gate' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Main Gate")
        elif (var13.get() == 'Uni Hospital' and var9.get() == 'Main Gate'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Main Gate")
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Main Gate' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Main Gate")

    #----------------------Travel cost calculation -Uni Hospital TO CSE Block (standard)--------------------------------------------------

        if (var13.get() == 'Uni Hospital' and var9.get() == 'CSE Block'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("CSE Block")

        elif (var13.get() == 'Uni Hospital' and var9.get() == 'CSE Block'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("CSE Block")
        if (var13.get() == 'Uni Hospital' and var9.get() == 'CSE Block'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("CSE Block")
    #------------------Travel cost calculation -Uni Hospital to CSE Block (mini)-------------------------------------------------
        if (var13.get() == 'Uni Hospital' and var9.get() == 'CSE Block' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("CSE Block")
        elif (var13.get() == 'Uni Hospital' and var9.get() == 'CSE Block'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("CSE Block")
        if (var13.get() == 'Uni Hospital' and var9.get() == 'CSE Block' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("CSE Block")

    #----------------------Travel cost calculation -Uni Hospital TO Uni Mall  (standard)--------------------------------------------------

        if (var13.get() == 'Uni Hospital' and var9.get() == 'Uni Mall'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Uni Mall")

        elif (var13.get() == 'Uni Hospital' and var9.get() == 'Uni Mall'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Uni Mall")
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Uni Mall'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Uni Mall")
    #------------------Travel cost calculation -Uni Hospital to Uni Mall (mini)-------------------------------------------------
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Uni Mall' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Uni Mall")
        elif (var13.get() == 'Uni Hospital' and var9.get() == 'Uni Mall'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Uni Mall")
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Uni Mall' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Uni Mall")

    #----------------------Travel cost calculation -Uni Hospital TO Girls Hostel  (standard)--------------------------------------------------

        if (var13.get() == 'Uni Hospital' and var9.get() == 'Girls Hostel'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Girls Hostel")

        elif (var13.get() == 'Uni Hospital' and var9.get() == 'Girls Hostel'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Girls Hostel")
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Girls Hostel'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Girls Hostel")
    #------------------Travel cost calculation -Uni Hospital to Girls Hostel (mini)-------------------------------------------------
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Girls Hostel' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Girls Hostel")
        elif (var13.get() == 'Uni Hospital' and var9.get() == 'Girls Hostel'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Girls Hostel")
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Girls Hostel' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Girls Hostel")

    #----------------------Travel cost calculation -Uni Hospital TO Mechanical Block  (standard)--------------------------------------------------

        if (var13.get() == 'Uni Hospital' and var9.get() == 'Mechanical Block'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Mechanical Block ")

        elif (var13.get() == 'Uni Hospital' and var9.get() == 'Mechanical Block'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Mechanical Block ")
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Mechanical Block'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Mechanical Block ")
    #------------------Travel cost calculation -Uni Hospital to Mechanical Block (mini)-------------------------------------------------
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Mechanical Block' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Mechanical Block ")
        elif (var13.get() == 'Uni Hospital' and var9.get() == 'Mechanical Block'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Mechanical Block ")
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Mechanical Block' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Mechanical Block ")

    #----------------------Travel cost calculation -Uni Hospital TO Boys Hostel  (standard)--------------------------------------------------

        if (var13.get() == 'Uni Hospital' and var9.get() == 'Boys Hostel'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Boys Hostel ")

        elif (var13.get() == 'Uni Hospital' and var9.get() == 'Boys Hostel'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Boys Hostel ")
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Boys Hostel'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Uni Hospital")
           To_Destination.set("Boys Hostel ")
    #------------------Travel cost calculation -Uni Hospital to Mechanical Block (mini)-------------------------------------------------
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Boys Hostel' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Boys Hostel ")
        elif (var13.get() == 'Uni Hospital' and var9.get() == 'Boys Hostel'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Boys Hostel ")
        if (var13.get() == 'Uni Hospital' and var9.get() == 'Boys Hostel' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Uni Hospital")
            To_Destination.set("Boys Hostel ")

    #-------------------------------------Calculation Main Gate TO Uni Mall(Standard)----------------------------
        if (var13.get() == 'Main Gate' and var9.get() == 'Uni Mall'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("Uni Mall")

        elif (var13.get() == 'Main Gate' and var9.get() == 'Uni Mall'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("Uni Mall")
        if (var13.get() == 'Main Gate' and var9.get() == 'Uni Mall'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("LPU MG")
           To_Destination.set("Uni Mall")
    #------------------Travel cost calculation -main gate to Uni Mall(mini)-------------------------------------------------
        if (var13.get() == 'Main Gate' and var9.get() == 'Uni Mall' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("LPU MG")
            To_Destination.set("GH")
        elif (var13.get() == 'Uni Mall' and var9.get() == 'Uni Mall'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("LPU MG")
            To_Destination.set("GH")
        if (var13.get() == 'Uni Mall' and var9.get() == 'Uni Mall' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Mini()
           From_Destination.set("LPU MG")
           To_Destination.set("Uni Mall")

    #----------------------Travel cost calculation -Uni Mall TO Main Gate (standard)--------------------------------------------------

        if (var13.get() == 'Uni Mall' and var9.get() == 'Main Gate'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Main Gate")

        elif (var13.get() == 'Uni Mall' and var9.get() == 'Main Gate'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Main Gate")
        if (var13.get() == 'Uni Mall' and var9.get() == 'Main Gate'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Main Gate")
    #------------------Travel cost calculation -Uni Mall to MAIN GATE (mini)-------------------------------------------------
        if (var13.get() == 'Uni Mall' and var9.get() == 'Main Gate' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Main Gate")
        elif (var13.get() == 'Uni Mall' and var9.get() == 'Main Gate'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Main Gate")
        if (var13.get() == 'Uni Mall' and var9.get() == 'Main Gate' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Main Gate")

    #----------------------Travel cost calculation -Uni Mall TO CSE Block (standard)--------------------------------------------------

        if (var13.get() == 'Uni Mall' and var9.get() == 'CSE Block'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("CSE Block")

        elif (var13.get() == 'Uni Mall' and var9.get() == 'CSE Block'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("CSE Block")
        if (var13.get() == 'Uni Mall' and var9.get() == 'CSE Block'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("CSE Block")
    #------------------Travel cost calculation -Uni Mall to CSE Block (mini)-------------------------------------------------
        if (var13.get() == 'Uni Mall' and var9.get() == 'CSE Block' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("CSE Block")
        elif (var13.get() == 'Uni Mall' and var9.get() == 'CSE Block'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("CSE Block")
        if (var13.get() == 'Uni Mall' and var9.get() == 'CSE Block' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("CSE Block")

    #----------------------Travel cost calculation -Uni Mall TO Girls Hostel  (standard)--------------------------------------------------

        if (var13.get() == 'Uni Mall' and var9.get() == 'Girls Hostel'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Girls Hostel")

        elif (var13.get() == 'Uni Mall' and var9.get() == 'Girls Hostel'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Girls Hostel")
        if (var13.get() == 'Uni Mall' and var9.get() == 'Girls Hostel'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Girls Hostel")
    #------------------Travel cost calculation -Uni Mall to Girls Hostel (mini)-------------------------------------------------
        if (var13.get() == 'Uni Mall' and var9.get() == 'Girls Hostel' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Girls Hostel")
        elif (var13.get() == 'Uni Mall' and var9.get() == 'Girls Hostel'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Girls Hostel")
        if (var13.get() == 'Uni Mall' and var9.get() == 'Girls Hostel' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Girls Hostel")

    #----------------------Travel cost calculation -Uni Mall TO Uni Hospital  (standard)--------------------------------------------------

        if (var13.get() == 'Uni Mall' and var9.get() == 'Uni Hospital'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Uni Hospital")

        elif (var13.get() == 'Uni Mall' and var9.get() == 'Uni Hospital'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Uni Hospital")
        if (var13.get() == 'Uni Mall' and var9.get() == 'Uni Hospital'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Uni Hospital")
    #------------------Travel cost calculation -GIRLS HOSTEL to Uni Hospital (mini)-------------------------------------------------
        if (var13.get() == 'Uni Mall' and var9.get() == 'Uni Hospital' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Uni Hospital")
        elif (var13.get() == 'Uni Mall' and var9.get() == 'Uni Hospital'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Uni Hospital")
        if (var13.get() == 'Uni Mall' and var9.get() == 'Uni Hospital' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Uni Hospital")

    #----------------------Travel cost calculation -Uni Mall TO Mechanical Block  (standard)--------------------------------------------------

        if (var13.get() == 'Uni Mall' and var9.get() == 'Mechanical Block'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Mechanical Block ")

        elif (var13.get() == 'Uni Mall' and var9.get() == 'Mechanical Block'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Mechanical Block ")
        if (var13.get() == 'Uni Mall' and var9.get() == 'Mechanical Block'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Mechanical Block ")
    #------------------Travel cost calculation -Uni Mall to Mechanical Block (mini)-------------------------------------------------
        if (var13.get() == 'Uni Mall' and var9.get() == 'Mechanical Block' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Mechanical Block ")
        elif (var13.get() == 'Uni Mall' and var9.get() == 'Mechanical Block'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Mechanical Block ")
        if (var13.get() == 'Uni Mall' and var9.get() == 'Mechanical Block' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Mechanical Block ")

    #----------------------Travel cost calculation -Uni Mall TO Boys Hostel  (standard)--------------------------------------------------

        if (var13.get() == 'Uni Mall' and var9.get() == 'Boys Hostel'  and var1.get() == 1 and var4.get() == 1 ):

           Travel_Cost_Adult_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Boys Hostel ")

        elif (var13.get() == 'Uni Mall' and var9.get() == 'Boys Hostel'  and var1.get() ==1 and var5.get() ==1):
           Travel_Cost_Child_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Boys Hostel ")
        if (var13.get() == 'Uni Mall' and var9.get() == 'Boys Hostel'  and var1.get() ==1 and var5.get() ==1 and var4.get()==1):
           Travel_Cost_Both_Calc_Standard()
           From_Destination.set("Uni Mall")
           To_Destination.set("Boys Hostel ")
    #------------------Travel cost calculation -Uni Mall to Mechanical Block (mini)-------------------------------------------------
        if (var13.get() == 'Uni Mall' and var9.get() == 'Boys Hostel' and var2.get() == 1 and var4.get() == 1 ):
            Travel_Cost_Adult_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Boys Hostel ")
        elif (var13.get() == 'Uni Mall' and var9.get() == 'Boys Hostel'  and var2.get() ==1 and var5.get() ==1):
            Travel_Cost_Child_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Boys Hostel ")
        if (var13.get() == 'Uni Mall' and var9.get() == 'Boys Hostel' and var2.get() ==1 and var5.get() ==1 and var4.get()==1):
            Travel_Cost_Both_Calc_Mini()
            From_Destination.set("Uni Mall")
            To_Destination.set("Boys Hostel ")
    Travel_Cost.has_been_called = False


    def chkbutton_value():

        if (var10.get() ==1):
            var12.set("")
            entSingle.configure(state=NORMAL)
        elif var10.get() ==0:
            entSingle.configure(state=DISABLED)
            var12.set("0")
        if (var11.get() ==1):
            var6.set("")
            entReturn.configure(state=NORMAL)
        elif var11.get()==0:
            entReturn.configure(state=DISABLED)
            var6.set("0")
    def Reset():
        qExit = messagebox.askyesno("Reset", "Do you want to Reset?")
        if qExit > 0:
            var1.set("0")
            var2.set("0")
            var3.set("0")
            var4.set("0")
            var5.set("0")
            var6.set("0")
            var7.set("")
            var8.set("0")
            var9.set(" ")
            var10.set("0")
            var11.set("0")
            var12.set("0")
            var13.set("")
            Tax.set("0")
            SubTotal.set("0")
            Total.set("0")
            CabType.set("")
            TicketPrice.set("")
            Child_Ticket.set("")
            Adult_Ticket.set("")
            From_Destination.set("")
            To_Destination.set("")
            Fee_Price.set("")
            var_result2.set("")
            var_result.set("")
            Receipt_Ref.set("")
            Route.set("")
            time1.set("")
            Date1.set("")
            btnTotal.config(state=NORMAL)
            entRemarks.config(state=NORMAL)
            btnBook.config(state=NORMAL)
            return


    #......................variables....................
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = StringVar()
    var8 = StringVar()
    var9 = StringVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = StringVar()
    Tax = StringVar()

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var5.set("0")
    var6.set("0") #6,10,11,12
    var7.set("")
    var8.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")


    SubTotal = StringVar()
    Total= StringVar()
    text_Input = StringVar()
    operator = ""


    #......................Create widget topLeftt1....................
    lblCabType = Label(topLeftt1, font=('arial', 22, 'bold'), text='Cab Type', width=20,height=1,bd=5)
    lblCabType.grid(row=0, column=0, sticky=W)

    chkStandard = Checkbutton(topLeftt1, font=('arial', 18, 'bold'), height=2,text='Standard', variable=var1, onvalue=1, offvalue=0)
    chkStandard.grid(row=1, column=0, sticky=W)

    chkMini = Checkbutton(topLeftt1, font=('arial', 18, 'bold'), height=2, text='Mini Cab', variable=var2, onvalue=1, offvalue=0)
    chkMini.grid(row=2, column=0, sticky=W)

    chkCampusTour = Checkbutton(topLeftt1, font=('arial', 18, 'bold'), height=2, text='Campus Tour', variable=var3, onvalue=1, offvalue=0)
    chkCampusTour.grid(row=3, column=0, sticky=W)

    #......................Create widget topLeftt2....................
    lblSelect = Label(topLeftt3, font=('arial', 20, 'bold'), text='Book Your Tickets', bd=8)
    lblSelect.grid(row=0, column=0, sticky=W, columnspan=2)
    lblDestination = Label(topLeftt3, font=('arial', 20, 'bold'), text='Destination', bd=4)
    lblDestination.grid(row=2, column=0, sticky=W)

    cboDestination = ttk.Combobox(topLeftt3, textvariable=var9, state='readonly', font=('arial', 12, 'bold'), width=16)
    cboDestination['value'] = ('', 'Boys Hostel', 'Girls Hostel', 'CSE Block', 'Mechanical Block', 'Uni Hospital','Uni Mall','Main Gate','Campus Tour')
    cboDestination.current(0)
    cboDestination.grid(row=2, column=1)


    lblFrom = Label(topLeftt3, font=('arial', 20, 'bold'), text='From', bd=4)
    lblFrom.grid(row=1, column=0, sticky=W)
    cboFrom = ttk.Combobox(topLeftt3, textvariable=var13, state='readonly', font=('arial', 12, 'bold'), width=16)
    cboFrom['value'] = ('', 'Main Gate', 'Girls Hostel', 'CSE Block', 'Mechanical Block', 'Uni Hospital','Uni Mall','Boys Hostel')
    cboFrom.current(0)
    cboFrom.grid(row=1, column=1)



    chkAdult = Checkbutton(topLeftt3, font=('arial', 20, 'bold'), text='Adult', variable=var4, onvalue=1, offvalue=0)
    chkAdult.grid(row=3, column=0, sticky=W)
    chkChild = Checkbutton(topLeftt3, font=('arial', 20, 'bold'), text='Child', variable=var5, onvalue=1, offvalue=0)
    chkChild.grid(row=4, column=0, sticky=W)

    #.........................Ticket.........................

    lblTicketType = Label(topLeftt2, font=('arial', 20, 'bold'), text='Ticket Type', bd=8)
    lblTicketType.grid(row=0, column=0, sticky=W)
    chkSingle = Checkbutton(topLeftt2, font=('arial', 20, 'bold'),height=2, text='Single', variable=var10, onvalue=1, offvalue=0,command=chkbutton_value)
    chkSingle.grid(row=1, column=0, sticky=W)
    entSingle = Entry(topLeftt2, font=('arial', 20, 'bold'), textvariable=var12, bd=2, width=8)
    entSingle.config(state=DISABLED)
    entSingle.grid(row=1, column=1, sticky=W)

    chkReturn = Checkbutton(topLeftt2, font=('arial', 20, 'bold'),height=1, text='Return', variable=var11, onvalue=1, offvalue=0,command=chkbutton_value)
    chkReturn.grid(row=2, column=0, sticky=W)

    entReturn = Entry(topLeftt2, font=('arial', 20, 'bold'), textvariable=var6, bd=2, width=8)
    entReturn.config(state=DISABLED)
    entReturn.grid(row=2, column=1, sticky=W)

    lblRemarks = Label(topLeftt2, font=('arial', 20, 'bold'), text='Remarks', bd=8)
    lblRemarks.grid(row=3, column=0, sticky=W)
    lblRemarks.config(state=NORMAL)
    entRemarks = Entry(topLeftt2, font=('arial', 16, 'bold'), textvariable=var7, bd=2, width=11)
    entRemarks.grid(row=3, column=1, sticky=W)
    entRemarks.config(state=NORMAL)


    #.....................Calculator..........
    text_Input = StringVar()
    txtDisplay = Entry(bottomLeftt2, font=('arial', 14, 'bold'), textvariable=text_Input, bd=8, bg="powder blue", justify='right')
    txtDisplay.grid(columnspan=4)

    btn7 = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="7", bg="powder blue", command=lambda: btnClick(7)).grid(row=2, column=0)

    btn8 = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="8", bg="powder blue", command=lambda: btnClick(8)).grid(row=2, column=1)

    btn9 = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="9", bg="powder blue", command=lambda: btnClick(9)).grid(row=2, column=2)

    Addition = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="+", bg="powder blue", command=lambda: btnClick("+")).grid(row=2, column=3)

    #.....................................

    btn4 = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="4", bg="powder blue", command=lambda: btnClick(4)).grid(row=3, column=0)


    btn5 = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="5", bg="powder blue", command=lambda: btnClick(5)).grid(row=3, column=1)


    btn6 = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="6", bg="powder blue", command=lambda: btnClick(6)).grid(row=3, column=2)

    Subtraction = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="-", bg="powder blue", command=lambda: btnClick("-")).grid(row=3, column=3)

    #.................................................................

    btn1 = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="1", bg="powder blue", command=lambda: btnClick(1)).grid(row=4, column=0)


    btn2 = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="2", bg="powder blue", command=lambda: btnClick(2)).grid(row=4, column=1)


    btn3 = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="3", bg="powder blue", command=lambda: btnClick(3)).grid(row=4, column=2)

    Multiply = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="*", bg="powder blue", command=lambda: btnClick("*")).grid(row=4, column=3)

    #--------------------------------------------------------------------
    btn0 = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="0", bg="powder blue", command=lambda: btnClick(0)).grid(row=5, column=0)


    btnClear = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="C", bg="powder blue", command=btnClearDisplay).grid(row=5, column=1)


    btnEquals = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="=", bg="powder blue", command=btnEqualsInput).grid(row=5, column=2)

    Division = Button(bottomLeftt2, padx=8, pady=8, bd=8, fg="black", font=('arial', 14, 'bold'), text="/", bg="powder blue", command=lambda: btnClick("/")).grid(row=5, column=3)

    #..................Tax,Subtotal and Total...........

    lblStateTax = Label(bottomLeftt1, font=('arial', 24, 'bold'), text="State Tax", bd=16, anchor='w')
    lblStateTax.grid(row=3, column=2)

    txtStateTax = Entry(bottomLeftt1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, width=28, bg="#ffffff", justify='right')
    txtStateTax.grid(row=3, column=3)


    lblSubTotal = Label(bottomLeftt1, font=('arial', 24, 'bold'), text="Sub Total", bd=16, anchor='w')
    lblSubTotal.grid(row=4, column=2)
    txtSubTotal = Entry(bottomLeftt1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, width=28, bg="#ffffff", justify='right')
    txtSubTotal.grid(row=4, column=3)

    lblTotalCost = Label(bottomLeftt1, font=('arial', 24, 'bold'), text="Total Cost", bd=16, anchor='w')
    lblTotalCost.grid(row=5, column=2)
    txtTotalCost = Entry(bottomLeftt1, font=('arial', 16, 'bold'), textvariable=Total, bd=16, width=28, bg="#ffffff", justify='right')
    txtTotalCost.grid(row=5, column=3)
    #......................................................
    lblSpace = Label(bottomLeftt1,font=('arial',24,'bold'),text = "      \n      ",bd=16,anchor='w')
    lblSpace.grid(row=6,column=2)
    lblSpace = Label(bottomLeftt2,font=('arial',24,'bold'),text = "      \n      ",bd=16,anchor='w')
    lblSpace.grid(row=6,columnspan=4)

    #------------------space---------------------------------
    lblRspace = Label(frameBottomRightt,font=('arial',12,'bold'),bd=2, anchor='w')
    lblRspace.grid(row=9,columnspan=4)

    lblRspace2 = Label(frameBottomRightt,width=40,height=3,bg="white",bd=8,font=('arial',11,'bold'),anchor='w')
    lblRspace2.grid(row=10,column=0,columnspan=4)

    #---------------------------------space----------------------
    lblsp = Label(frameBottomRightt,font=('arial',14,'bold'),bd=2,anchor='w')
    lblsp.grid(row=9,column=0,columnspan=4)
    #--------------------------------Button------------------------
    btnTotal = Button(frameBottomRightt,text='Total',padx=2,pady=2,bd=3,fg="red",font=('arial',26,'bold'),width=12,height=1,command=Travel_Cost)
    btnTotal.grid(row=10,column=0)
    btnTotal.config(state=NORMAL)

    btnReset = Button(frameBottomRightt,text='Reset',padx=2,pady=2,bd=3,fg="red",font=('arial',26,'bold'),width=8,height=1,command=Reset).grid(row=10,column=2)
    btnBook = Button(frameBottomRightt,text='Book',padx=2,pady=2,bd=3,fg="red",font=('arial',26,'bold'),width=8,height=1,command=Booking_confirmation)
    btnBook.grid(row=10,column=1)
    btnBook.config(state=NORMAL)

    btnExit = Button(frameBottomRightt,text='Exit',padx=2,pady=2,bd=3,fg="red",font=('arial',26,'bold'),width=8,height=1,command=iExit).grid(row=10,column=3)
    #...................
    lblsp = Label(frameBottomRightt,font=('arial',14,'bold'),bd=4,anchor='w',)
    lblsp.grid(row=11,column=0,columnspan=4)
    #-------------------

    return



afterLogin()
