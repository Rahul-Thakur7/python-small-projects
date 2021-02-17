from tkinter import*
from Login import *
t=Tk()
t.geometry("600x400")
t.resizable(0,0)
t.title("Homepage of Registration form")
def home():
            f1=Frame(bg="blue")
            f1.place(x=0,y=0,width=600,height=400)
            B1=Button(f1,text="Login",command=login)
            B1.place(x=220,y=100,width=80, height=40)
            B2=Button(f1,text="Regis",command=regis)
            B2.place(x=310,y=100,width=80,height=40)

home()
t.mainloop()
