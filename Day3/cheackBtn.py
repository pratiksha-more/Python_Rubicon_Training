from tkinter import messagebox
from tkinter import *

top = Tk()
top.title("My First GUI")
top.geometry("500x500")
top['bg'] = '#87Ceeb'


def check():
    str=" "

    if checkVar1.get() == 1:
        str =str+ " Python"
    if checkVar2.get() == 1:
        str =str+ " Java"
    if checkVar3.get() == 1:
        str =str+ " C++"
    if checkVar4.get() == 1:
        str =str+ " C#"

    messagebox.showinfo("Result", f"Selected Languages: {str}")

checkVar1 = IntVar()
checkVar2 = IntVar()    
checkVar3 = IntVar()
checkVar4 = IntVar()

checkbutton1 = Checkbutton(top, text="Python", variable=checkVar1, onvalue=1, offvalue=0).place(x=20, y=20)
checkbutton2 = Checkbutton(top, text="Java", variable=checkVar2, onvalue=1, offvalue=0).place(x=20, y=60)
checkbutton3 = Checkbutton(top, text="C++", variable=checkVar3, onvalue=1, offvalue=0).place(x=20, y=100)
checkbutton4 = Checkbutton(top, text="C#", variable=checkVar4, onvalue=1, offvalue=0).place(x=20, y=140)    

button = Button(top, text="Check", command=check, bg="orange").place(x=100, y=180)

top.mainloop()  
