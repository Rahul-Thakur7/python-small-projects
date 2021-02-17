from tkinter import *
import sqlite3
root = Tk()
root.configure(bg='sky blue')
root.geometry("400x400")

root.title("Login page")
a=StringVar()
b=StringVar()

def login():
        db=sqlite3.connect('MUKUND.db')
        cr=db.cursor()
        cr.execute("insert into login values('"+a.get()+"', '"+b.get()+"')")
        db.commit()
        db.close()
        print("Data insert..")
        a.set("")
        b.set("")


L1=Label( text="ENTER NAME",font=("",10),bg='sky blue')
L1.place(x=100,y=50)

#Entry box of 1st label
e1 = Entry(font=("",10), textvariable=a)
#e1.pack()
e1.place(x=200,y=50)

#2nd label
L2 = Label(text="PASSWARD",font=("",10),bg='sky blue')
L2.place(x=100,y=100)

#Entry box for password
e2 = Entry(font=("",10), textvariable=b)
e2.place(x=200,y=100)
#e2.pack()

#login button
B=Button(text="login",font=("Arial",20),command=login)
B.place(x=200,y=150,width=80,height=40)

#print("Login Succsesful")
root.mainloop()
