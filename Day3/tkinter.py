import tkinter

top = tkinter.Tk()

top.title("My First GUI")
top.geometry("500x500")
top['bg'] = '#87Ceeb'  # Light blue background color

label = tkinter.Label(top, text="UserName : ").place(x=20, y=20)
entry = tkinter.Entry(top).place(x=110, y=20)

label = tkinter.Label(top, text="Password : ").place(x=20, y=60)
entry = tkinter.Entry(top).place(x=110, y=60)

button = tkinter.Button(top, text="Click Me", command=lambda: print("Button clicked!")).place(x=100,y=90)




top.mainloop()
