from tkinter import messagebox
from tkinter import *

top = Tk()
top.title("My First GUI")
top.geometry("500x500")
top['bg'] = '#87Ceeb'  

Label(top, text="My Favourite Fruites Are : ", ).place(x=20, y=20)

listbox=Listbox(top, selectmode=MULTIPLE, height=5, width=20)
listbox.insert(1, "Apple")
listbox.insert(2, "Banana") 
listbox.insert(3, "Cherry")
listbox.insert(4, "Mango")
listbox.insert(5, "Orange")


listbox.place(x=20, y=50)
top.mainloop()
