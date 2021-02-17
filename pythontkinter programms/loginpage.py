from tkinter import *
from  tkinter import Button

def login():
    root =Tk()
    root.configure(bg='sky blue')
    root.geometry("600x400")
    root.resizable(0,0)
    root.title("Loginpage")

    L1 =Label(text="ENTER NAME",font=("",10),bg='sky blue')
    L1.place(x=180,y=120)


    E1 =Entry(font=("",10))
    E1.place(x=300,y=120)

    L2 =Label(text="PASSWARD",font=("",10),bg='sky blue')
    L2.place(x=180,y=160)

    E2 = Entry(font=("",10))
    E2.place(x=300,y=160)

    B=Button(text="login",font=("Arial",20),command=login)
    B.place(x=280,y=200,width=80,height=40)


def regis():

           root =Tk()
           root.configure(bg='blue')
           root.geometry("600x400")
           root.resizable(0,0)
           root.title("Registration page")
 
           L=Label(text="ENTER NAME",font=("",10),bg='blue')
           L.place(x=180,y=100)


           L1 =Entry(font=("",10))
           L1.place(x=300,y=100)


           L3 =Label(text="ENTER EMAIL",font=("",10),bg='blue')
           L3.place(x=180,y=150)


           E1 =Entry(font=("",10))
           E1.place(x=300,y=150)


           L2 =Label(text="PASSWORD",font=("",10),bg='blue')
           L2.place(x=180,y=200)


           E2 =Entry(font=("",10))
           E2.place(x=300,y=200)

   
           B=Button(text="Register",font=("Arial",15),command=regis)
           B.place(x=280,y=250,width=80,height=40)


