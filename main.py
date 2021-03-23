from tkinter import *
import tkinter.messagebox
import sqlite3

class Product:
    def __init__(self,root):
        self.root=root
        self.root.title("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM")
        self.root.geometry("1325x690")
        self.root.config(bg="grey")

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


if __name__== '__main__':
    root=Tk()
    application=Product(root)
    root.mainloop()

