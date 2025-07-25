from tkinter import *
from tkinter import messagebox

top= Tk()
top.title("My First GUI")
top.geometry("500x500")
top['bg'] = '#87Ceeb'  # Light blue background color

def scale():
    sel="Selected Value: " + str(var.get())
    label.config(text=sel)

var= IntVar()


Scale(top, from_=0, to=100, orient=HORIZONTAL, variable=var, command=lambda x: scale()).pack(anchor=CENTER, pady=20)
Button(top, text="Show Value", command=scale, bg="orange").pack(anchor=CENTER, pady=10)
label=Label(top, text="Selected Value: 0", bg='#87Ceeb')
label.pack()

top.mainloop()
