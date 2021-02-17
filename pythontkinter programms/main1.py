import os
from subprocess import call

import sys
from tkinter import *

def click_checkinn():
    call(["python", "checkin.py"])
def click_list():
    call(["python", "list.py"])
def click_checkout():
    call(["python", "checkout.py"])
def click_getinfo():
    call(["python","getinfoui.py"])


class HOTEL_MANAGEMENT:
    def __init__(self):
        root = Tk()
        
        _bgcolor = 'white' 
        _fgcolor = 'black' 
        _compcolor = 'white' 
        _ana1color = 'white' 
        _ana2color = 'white' 
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("700x700")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="white")
        root.configure(highlightbackground="white")
        root.configure(highlightcolor="black")



        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="white")
        self.Frame1.configure(highlightbackground="white")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
        self.Message6.configure(background="white")
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="white")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''WELCOME''')
        self.Message6.configure(width=791)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.18, rely=0.17, height=103, width=566)
        self.Button2.configure(activebackground="white")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="white")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="white")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''1.CHECK INN''')
        self.Button2.configure(width=566)
        self.Button2.configure(command=click_checkinn)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.18, rely=0.33, height=93, width=566)
        self.Button3.configure(activebackground="white")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="white")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="white")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''2.SHOW GUEST LIST''')
        self.Button3.configure(width=566)
        self.Button3.configure(command=click_list)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.18, rely=0.47, height=93, width=566)
        self.Button4.configure(activebackground="white")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="white")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="white")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''3.CHECK OUT''')
        self.Button4.configure(width=566)
        self.Button4.configure(command=click_checkout)

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.18, rely=0.61, height=103, width=566)
        self.Button5.configure(activebackground="white")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="white")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font14)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="white")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''4.GET INFO ''')
        self.Button5.configure(width=566)
        self.Button5.configure(command=click_getinfo)

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.18, rely=0.77, height=103, width=566)
        self.Button6.configure(activebackground="white")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="white")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(font=font14)
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="white")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''5.EXIT''')
        self.Button6.configure(width=566)
        self.Button6.configure(command=quit)
        root.mainloop()
if __name__ == '__main__':
    GUUEST=HOTEL_MANAGEMENT()


