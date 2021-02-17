from tkinter import *
def clicked():
    lbl5.configure("Welcome " + lbl3.get())

window = Tk()
window.geometry('350x200')
window.title("Welcome To Home")
lbl3 = Entry(window, text="Name",font=("",30),bg='green',command=clicked,fg='red')
lbl3.grid(column=0,columnspan=2, row=2,pady=20)

lbl5 = Entry(window, text=" ",font=("",30),bg='green',command=clicked,fg='red')
lbl5.grid(column=0,columnspan=2, row=2,pady=20)

lbl4 = Button(window, text="Login",font=("",30),bg='green',command=clicked)
lbl4.grid(column=0,columnspan=2, row=2,pady=20)

window.mainloop()
