from tkinter import *

def login():
    
    window = Tk()

    window.title("Welcome ")

    lbl = Label(window, text="Name",font=("",30),bg='green')
    lbl.grid(column=0, row=0,sticky='w',pady=20)

    lbl1 = Label(window, text="Password",font=("",30),bg='green')
    lbl1.grid(column=0, row=1,pady=20)

    lbl2 = Entry(window, text="Name",font=("",30),bg='green')
    lbl2.grid(column=1, row=0,sticky='w',pady=20)

    lbl3 = Entry(window, text="Password",font=("",30),bg='green')
    lbl3.grid(column=1, row=1,pady=20)

    lbl3 = Button(window, text="Login",font=("",30),bg='green')
    lbl3.grid(column=0,columnspan=2, row=2,pady=20)

    window.mainloop()
login()
