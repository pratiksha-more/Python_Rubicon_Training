from tkinter import messagebox
from tkinter import *

top=Tk()

top.title("My First GUI")
top.geometry("500x500")
top['bg'] = '#87Ceeb'  # Light blue background color

def add():
    firstname = int(firstNum.get())
    lastname = int(lastNum.get())

    messagebox.showinfo("Result", f"Sum: {firstname + lastname}")

#declaring Variables
firstNum=IntVar()
lastNum=IntVar()

Label(top, text="First Number: ",width="13").place(x=20, y=20)
Label(top, text="Second Number: ",width="13").place(x=20, y=60)
Entry(top, textvariable=firstNum).place(x=150, y=20)
Entry(top, textvariable=lastNum).place(x=150, y=60)

Button(top, text="Add", command=add,bg="orange").place(x=100, y=100)
top.mainloop()

