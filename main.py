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

        rightbodyframe = LabelFrame(bodyframe, bd=2, width=400, height=380,
                                   padx=20, pady=10, bg="grey", relief=RIDGE, font=("arial", 15, "bold"),
                                   text="Product Item Information:")
        rightbodyframe.pack(side=RIGHT)

        self.labelpId=Label(leftbodyframe,font=("arial",15,"bold"),text="Product Id : ",padx=2,bg="white",fg=
                            "blue")
        self.labelpId.grid(row=0,column=0,sticky=W)
        self.textpId=Entry(leftbodyframe,font=("arial",15,"bold"),textvariable=pId,width=35)
        self.textpId.grid(row=0,column=1,sticky=W)

        self.labelpName = Label(leftbodyframe, font=("arial", 15, "bold"), text="Product Name : ", padx=2, bg="white", fg=
        "blue")
        self.labelpName.grid(row=1, column=0, sticky=W)
        self.textpName = Entry(leftbodyframe, font=("arial", 15, "bold"), textvariable=pName, width=35)
        self.textpName.grid(row=1, column=1, sticky=W)

        self.labelpPrice = Label(leftbodyframe, font=("arial", 15, "bold"), text="Product Price : ", padx=2, bg="white", fg=
        "blue")
        self.labelpPrice.grid(row=2, column=0, sticky=W)
        self.textpPrice = Entry(leftbodyframe, font=("arial", 15, "bold"), textvariable=pPrice, width=35)
        self.textpPrice.grid(row=2, column=1, sticky=W)

        self.labelpQty = Label(leftbodyframe, font=("arial", 15, "bold"), text="Product Quantity : ", padx=2, bg="white", fg=
        "blue")
        self.labelpQty.grid(row=3, column=0, sticky=W)
        self.textpQty = Entry(leftbodyframe, font=("arial", 15, "bold"), textvariable=pQty , width=30)
        self.textpQty.grid(row=3, column=1, sticky=W)

        self.labelpCompany = Label(leftbodyframe, font=("arial", 15, "bold"), text="MFG. Company : ", padx=2, bg="white", fg=
        "blue")
        self.labelpCompany.grid(row=4, column=0, sticky=W)
        self.textpCompany = Entry(leftbodyframe, font=("arial", 15, "bold"), textvariable=pCompany, width=30)
        self.textpCompany.grid(row=4, column=1, sticky=W)

        self.labelpContact = Label(leftbodyframe, font=("arial", 15, "bold"), text="Company contact : ", padx=2, bg="white", fg=
        "blue")
        self.labelpContact.grid(row=5, column=0, sticky=W)
        self.textpContact = Entry(leftbodyframe, font=("arial", 15, "bold"), textvariable=pContact, width=30)
        self.textpContact.grid(row=5, column=1, sticky=W)


        scroll=Scrollbar(rightbodyframe)
        scroll.grid(row=0,column=1,sticky="ns")
        productList=Listbox(rightbodyframe,width=36,height=15,font=("arial",12,"bold"),
                            yscrollcommand=scroll.set)
        productList.grid(row=0,column=0,padx=8)
        scroll.config(command=productList.yview())

        self.buttonsave = Button(operationframe, text="Save", font=("arial", 20, "bold"), height=1,
                                 width=10, bd=4)
        self.buttonsave.grid(row=0, column=0)

        self.buttonshow = Button(operationframe, text="Show", font=("arial", 20, "bold"), height=1,
                                 width=10, bd=4)
        self.buttonshow.grid(row=0, column=1)

        self.buttonclear = Button(operationframe, text="Clear", font=("arial", 20, "bold"), height=1,
                                 width=10, bd=4)
        self.buttonclear.grid(row=0, column=2)

        self.buttondelete = Button(operationframe, text="Delete", font=("arial", 20, "bold"), height=1,
                                 width=10, bd=4)
        self.buttondelete.grid(row=0, column=3)

        self.buttonsearch = Button(operationframe, text="Search", font=("arial", 20, "bold"), height=1,
                                 width=10, bd=4)
        self.buttonsearch.grid(row=0, column=4)

        self.buttonupdate = Button(operationframe, text="Update", font=("arial", 20, "bold"), height=1,
                                 width=10, bd=4)
        self.buttonupdate.grid(row=0, column=5)

        self.buttonclose = Button(operationframe, text="Close", font=("arial", 20, "bold"), height=1,
                                 width=10, bd=4)
        self.buttonclose.grid(row=0, column=5)


class Database:
    def conn(self):
        print("Database : connection method called")
        con=sqlite3.connect("Inventory.db")
        cur=con.cursor()
        query="create a table if not exists product(pid integer primary key,pname text,price text,qty text,company text,contact text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : connection method finished")

    def insert(self,pid,pname,price,qty,company,contact):
        print("Database : insert method called")
        con = sqlite3.connect("Inventory.db")
        cur = con.cursor()
        query="insert into product values(?,?,?,?,?,?)"
        cur.execute(query,(pid,pname,price,qty,company,contact))
        con.commit()
        con.close()
        print("Database : connection method finished")

    def show(self):
        print("Database : show method called")
        con = sqlite3.connect("Inventory.db")
        cur = con.cursor()
        query="select * from product"
        cur.execute(query)
        rows=cur.fetchall()
        con.close()
        print("Database : show method finished")
        return rows

    def deletee(self,pid):
        print("Database : delete method called",pid)
        con = sqlite3.connect("Inventory.db")
        cur = con.cursor()
        cur.execute("delete from product where pid=?",(pid,))
        con.commit()
        con.close()
        print(pid,"Database : delete method finished")

    def search(self,pid="",pname="",price="",qty="",company="",contact=""):
        print("Database : search method called", pid)
        con = sqlite3.connect("Inventory.db")
        cur = con.cursor()
        cur.execute("delete from product where pid=? or pname=? or price=? or \
                    qty=? or company=? or contact=?")
        row=cur.fetchall()
        con.close()
        print(pid,"Database : delete method finished")
        return row

    def update(self,pid="",pname="",price="",qty="",company="",contact=""):
        con = sqlite3.connect("Inventory.db")
        cur = con.cursor()
        cur.execute("update  product set pid=? or pname=? or price=? or \
                            qty=? or company=? or contact=? where pid=?",(pid,pname,price,qty,company,contact,pid))
        con.commit()
        con.close()
        print(pid,"Database : delete method finished")












if __name__== '__main__':
    root=Tk()
    application=Product(root)
    root.mainloop()

