from tkinter import *    
from tkinter import messagebox

def submit():
    messagebox.showinfo("Submitted", "Form Submitted Successfully!")

top = Tk()
top.title("College Application Form")
top.geometry("500x500")
#top['bg'] = '#87Ceeb'  # Light blue

Label(top, text="College Application Form").place(x=170, y=20)

# Name
Label(top, text="Name:").place(x=50, y=50)
Entry(top).place(x=200, y=50)

# Roll No
Label(top, text="Roll No:").place(x=50, y=90)
Entry(top).place(x=200, y=90)

# Year (Checkboxes)
Label(top, text="Year:").place(x=50, y=130)
var1 =IntVar()
var2=IntVar()
var3 =IntVar()
var4=IntVar()
Checkbutton(top, text="FE", variable=var1).place(x=200, y=130)
Checkbutton(top, text="SE", variable=var2).place(x=250, y=130)
Checkbutton(top, text="TE", variable=var3).place(x=300, y=130)
Checkbutton(top, text="BE", variable=var4).place(x=350, y=130)

# College Name
Label(top, text="College Name:").place(x=50, y=170)
Entry(top).place(x=200, y=170)

# Branch (Dropdown)
Label(top, text="Branch:").place(x=50, y=210)
branch = StringVar()
branch.set("Select Branch")
OptionMenu(top, branch, "Computer", "IT", "Mechanical", "Civil").place(x=200, y=210)

# Submit Button
Button(top, text="Submit", command=submit).place(x=200, y=260)

top.mainloop()
