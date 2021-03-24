from tkinter import *
import tkinter.messagebox
import sqlite3

class Product:
    def __init__(self,root):
        self.root=root
        self.root.title("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM")
        self.root.geometry("1325x690")
        self.root.config(bg="grey")

        pId=StringVar
        pName=StringVar
        pPrice=StringVar
        pQty=StringVar
        pCompany=StringVar
        pContact=StringVar



        MainFrame = Frame(self.root,bg="red")
        MainFrame.grid()

        HeadFrame=Frame(MainFrame,bd=1,padx=50,pady=10,
                        bg='white',relief=RIDGE)
        HeadFrame.pack(side=TOP)

        self.ITitle=Label(HeadFrame,font=('arial',50,'bold'),
                          fg='red',text="Warehouse Inventory Sales Purchase",
                           bg="white")
        self.ITitle.grid()
        operationframe=Frame(MainFrame,bd=2,width=1300,height=60,
                             padx=50,pady=20,bg="white",relief=RIDGE)
        operationframe.pack(side=BOTTOM)

        bodyframe = Frame(MainFrame, bd=2, width=1290, height=400,
                               padx=50, pady=20, bg="white", relief=RIDGE)
        bodyframe.pack(side=BOTTOM)
        leftbodyframe=LabelFrame(bodyframe, bd=2, width=600, height=380,
                               padx=20, pady=10, bg="grey", relief=RIDGE,font=("arial",15,"bold"),
                                 text="Product Item Details:")
        leftbodyframe.pack(side=LEFT)

        rightbodyframe = LabelFrame(bodyframe, bd=2, width=300, height=380,
                                   padx=20, pady=10, bg="grey", relief=RIDGE, font=("arial", 15, "bold"),
                                   text="Product Item Information:")
        rightbodyframe.pack(side=RIGHT)

        self.labelpId=Label(leftbodyframe,font=("arial",15,"bold"),text="Product Id",padx=2,bg="white",fg=
                            "blue")
        self.labelpId.grid(row=0,column=0,sticky=W)
        self.textpId=Entry(leftbodyframe,font=("arial",15,"bold"),textvariable=pId,width=35)
        self.textpId.grid(row=0,column=1,sticky=W)

        self.labelpName = Label(leftbodyframe, font=("arial", 15, "bold"), text="Product Name", padx=2, bg="white", fg=
        "blue")
        self.labelpName.grid(row=1, column=0, sticky=W)
        self.textpName = Entry(leftbodyframe, font=("arial", 15, "bold"), textvariable=pName, width=35)
        self.textpName.grid(row=1, column=1, sticky=W)

        self.labelpPrice = Label(leftbodyframe, font=("arial", 15, "bold"), text="Product Price", padx=2, bg="white", fg=
        "blue")
        self.labelpPrice.grid(row=2, column=0, sticky=W)
        self.textpPrice = Entry(leftbodyframe, font=("arial", 15, "bold"), textvariable=pId, width=35)
        self.textpPrice.grid(row=2, column=1, sticky=W)

        self.labelpId = Label(leftbodyframe, font=("arial", 15, "bold"), text="Product Id", padx=2, bg="white", fg=
        "blue")
        self.labelpId.grid(row=0, column=0, sticky=W)
        self.textpId = Entry(leftbodyframe, font=("arial", 15, "bold"), textvariable=pId, width=35)
        self.textpId.grid(row=0, column=1, sticky=W)

        self.labelpId = Label(leftbodyframe, font=("arial", 15, "bold"), text="Product Id", padx=2, bg="white", fg=
        "blue")
        self.labelpId.grid(row=0, column=0, sticky=W)
        self.textpId = Entry(leftbodyframe, font=("arial", 15, "bold"), textvariable=pId, width=35)
        self.textpId.grid(row=0, column=1, sticky=W)

        self.labelpId = Label(leftbodyframe, font=("arial", 15, "bold"), text="Product Id", padx=2, bg="white", fg=
        "blue")
        self.labelpId.grid(row=0, column=0, sticky=W)
        self.textpId = Entry(leftbodyframe, font=("arial", 15, "bold"), textvariable=pId, width=35)
        self.textpId.grid(row=0, column=1, sticky=W)


if __name__== '__main__':
    root=Tk()
    application=Product(root)
    root.mainloop()

