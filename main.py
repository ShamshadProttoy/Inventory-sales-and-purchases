from tkinter import *
import tkinter.messagebox
import sqlite3

class Product:
    def __init__(self,root):
        self.root=root
        self.root.title("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM")
        self.root.geometry("1325x690")
        self.root.config(bg="grey")


if __name__== '__main__':
    root=Tk()
    application=Product(root)
    root.mainloop()
