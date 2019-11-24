#fronted
from tkinter import *
import tkinter.messagebox
import Database_A


class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Customer Database Management System")
        self.root.geometry("1350x650+0+0")
        self.root.resizable(FALSE, FALSE)
        self.root.iconbitmap('Management.ico')

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoR = StringVar()
        DoD = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        # ======================================================Frames=============
        def iExit():
            iExit = tkinter.messagebox.askyesno("Customer Database Management System",  "Confirm if you Want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.textstdID.delete(0,END)
            self.textfna.delete(0,END)
            self.textsna.delete(0,END)
            self.textDoR.delete(0,END)
            self.textDoD.delete(0,END)
            self.textAge.delete(0,END)
            self.textGender.delete(0,END)
            self.textAddress.delete(0,END)
            self.textMobile.delete(0,END)

        def addData():
            if(len(StdID.get())!=0):
                Database_A.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoR.get(), DoD.get(),\
                                     Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(), Firstname.get(), Surname.get(), DoR.get(), DoD.get(),\
                     Age.get(), Gender.get(), Address.get(), Mobile.get()))

        def DisplayData():
            studentlist.delete(0,END)
            for row in Database_A.viewData():
                studentlist.insert(END,row,str(""))

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.textstdID.delete(0, END)
            self.textstdID.insert(END, sd[1])
            self.textfna.delete(0, END)
            self.textfna.insert(END, sd[2])
            self.textsna.delete(0, END)
            self.textsna.insert(END, sd[3])
            self.textDoR.delete(0, END)
            self.textDoR.insert(END, sd[4])
            self.textDoD.delete(0, END)
            self.textDoD.insert(END, sd[5])
            self.textAge.delete(0, END)
            self.textAge.insert(END, sd[6])
            self.textGender.delete(0, END)
            self.textGender.insert(END, sd[7])
            self.textAddress.delete(0, END)
            self.textAddress.insert(END, sd[8])
            self.textMobile.delete(0, END)
            self.textMobile.insert(END, sd[9])

        def DeleteData():
            if(len(StdID.get()) !=0):
                Database_A.deleteRec(sd[0])
                clearData()
                DisplayData()


        def searchDatabase():
            studentlist.delete(0,END)
            for row in Database_A.searchData(StdID.get(), Firstname.get(), Surname.get(), DoR.get(), DoD.get(),\
                                             Age.get(), Gender.get(), Address.get(), Mobile.get()):
                studentlist.insert(END,row,str(""))

        def update():
            if(len(StdID.get()) !=0):
                Database_A.deleteRec(sd[0])
            if(len(StdID.get()) !=0):
                Database_A.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoR.get(), DoD.get(),\
                                     Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0, END)
                studentlist.insert(END,(StdID.get(), Firstname.get(), Surname.get(), DoR.get(), DoD.get(),\
                                     Age.get(), Gender.get(), Address.get(), Mobile.get()))

        #======================================================Frames=============
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost white", relief=RAISED)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font="arial 47 bold", text="Customer Database Management System", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost white", relief=RAISED)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame= Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RAISED, bg="Cadet blue")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RAISED, bg="Ghost white",
                                  font="arial 20 bold", text="Customer Info: App Creator. Md. Al Amin Sarkar.\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RAISED, bg="Ghost white",
                                   font="arial 20 bold", text="Customer Details:\n")
        DataFrameRIGHT.pack(side=RIGHT)
        # ======================================================Labels and Entry Eidget=============

        self.lblstdID = Label(DataFrameLEFT, font="arial 20 bold", text="Customer ID:", padx=2, pady=2, bg="Ghost White")
        self.lblstdID.grid(row=0, column=0, sticky=W)

        self.textstdID = Entry(DataFrameLEFT, font="arial 20 bold",textvariable=StdID, width=39)
        self.textstdID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font="arial 20 bold", text="First Name:", padx=2, pady=2, bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)

        self.textfna = Entry(DataFrameLEFT, font="arial 20 bold", textvariable=Firstname, width=39)
        self.textfna.grid(row=1, column=1)

        self.lblsna = Label(DataFrameLEFT, font="arial 20 bold", text="Surname:", padx=2, pady=2, bg="Ghost White")
        self.lblsna.grid(row=2, column=0, sticky=W)

        self.textsna = Entry(DataFrameLEFT, font="arial 20 bold", textvariable=Surname, width=39)
        self.textsna.grid(row=2, column=1)

        self.lblDoR = Label(DataFrameLEFT, font="arial 20 bold", text="Date of Receive:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblDoR.grid(row=3, column=0, sticky=W)

        self.textDoR = Entry(DataFrameLEFT, font="arial 20 bold", textvariable=DoR, width=39)
        self.textDoR.grid(row=3, column=1)

        self.lblDoD = Label(DataFrameLEFT, font="arial 20 bold", text="Date of Delivery:", padx=2, pady=2, bg="Ghost White")
        self.lblDoD.grid(row=4, column=0, sticky=W)

        self.textDoD = Entry(DataFrameLEFT, font="arial 20 bold", textvariable=DoD, width=39)
        self.textDoD.grid(row=4, column=1)

        self.lblAge = Label(DataFrameLEFT, font="arial 20 bold", text="Age:", padx=2, pady=2, bg="Ghost White")
        self.lblAge.grid(row=5, column=0, sticky=W)

        self.textAge = Entry(DataFrameLEFT, font="arial 20 bold", textvariable=Age, width=39)
        self.textAge.grid(row=5, column=1)

        self.lblGender = Label(DataFrameLEFT, font="arial 20 bold", text="Gender:", padx=2, pady=2, bg="Ghost White")
        self.lblGender.grid(row=6, column=0, sticky=W)

        self.textGender = Entry(DataFrameLEFT, font="arial 20 bold", textvariable=Gender, width=39)
        self.textGender.grid(row=6, column=1)

        self.lblAddress = Label(DataFrameLEFT, font="arial 20 bold", text="Address:", padx=2, pady=2, bg="Ghost White")
        self.lblAddress.grid(row=7, column=0, sticky=W)

        self.textAddress = Entry(DataFrameLEFT, font="arial 20 bold", textvariable=Address, width=39)
        self.textAddress.grid(row=7, column=1)

        self.lblMobile = Label(DataFrameLEFT, font="arial 20 bold", text="Mobile:", padx=2, pady=2, bg="Ghost White")
        self.lblMobile.grid(row=8, column=0, sticky=W)

        self.textMobile = Entry(DataFrameLEFT, font="arial 20 bold", textvariable=Mobile, width=39)
        self.textMobile.grid(row=8, column=1)

        # ======================================================List Box and Scrollbar Widget========================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')
        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font="arial 12 bold", yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = studentlist.yview)

        # ======================================================Button Widget========================
        self.btnAddData = Button(ButtonFrame, text="Add New", font="arial 20 bold", width=10, height=1, bd=4, fg="Green", command=addData)
        self.btnAddData.grid(row=0, column=0)
        self.btnDisplayDate = Button(ButtonFrame, text="Display", font="arial 20 bold", width=10, height=1, bd=4, fg="Orange", command=DisplayData)
        self.btnDisplayDate.grid(row=0, column=1)
        self.btnClearData = Button(ButtonFrame, text="Clear", font="arial 20 bold", width=10, height=1, bd=4, fg="Red", command=clearData)
        self.btnClearData.grid(row=0, column=2)
        self.btnDeleteData = Button(ButtonFrame, text="Delete", font="arial 20 bold", width=10, height=1, bd=4, fg="Red", command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)
        self.btnSearchData = Button(ButtonFrame, text="Search", font="arial 20 bold", width=10, height=1, bd=4, fg="Green", command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)
        self.btnUpdateData = Button(ButtonFrame, text="Update", font="arial 20 bold", width=10, height=1, bd=4, fg="Magenta", command=update)
        self.btnUpdateData.grid(row=0, column=5)
        self.btnExit = Button(ButtonFrame, text="Exit", font="arial 20 bold", width=10, height=1, bd=4, fg="#3df00c", command=iExit)
        self.btnExit.grid(row=0, column=6)
if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()