#Ruben Jr. Mendez Rodriguez #120980
#We started with the first part the simple game and now we work it to be a GUI
#The game instructions are in the README
	

from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import font


def buttonpress1(b1):
    b1["text"]="M"
    if (b2["text"]=="N" and b3["text"]=="T") or (b4["text"]=="C" and b7["text"]=="H") or (b5["text"]=="A" and b9["text"]=="W") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress2(b2):
    b2["text"]="A"
    if (b1["text"]=="A" and b3["text"]=="T") or (b5["text"]=="A" and b8["text"]=="O") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress3(b3):
    b3["text"]="P"
    if (b2["text"]=="N" and b1["text"]=="A") or (b6["text"]=="N" and b9["text"]=="W") or (b5["text"]=="A" and b7["text"]=="H") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress4(b4):
    b4["text"]="W"
    if (b1["text"]=="A" and b7["text"]=="H") or (b5["text"]=="A" and b6["text"]=="N") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress5(b5):
    b5["text"]="I"
    if (b2["text"]=="N" and b8["text"]=="O") or (b4["text"]=="C" and b6["text"]=="N") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress6(b6):
    b6["text"]="N"
    if (b3["text"]=="I" and b9["text"]=="W") or (b4["text"]=="C" and b5["text"]=="A") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress7(b7):
    b7["text"]="B"
    if (b1["text"]=="A" and b4["text"]=="C") or (b8["text"]=="O" and b9["text"]=="W") or (b5["text"]=="A" and b3["text"]=="T") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress8(b8):
    b8["text"]="O"
    if (b2["text"]=="N" and b5["text"]=="A") or (b7["text"]=="H" and b9["text"]=="W") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress9(b9):
    b9["text"]="X"
    if (b6["text"]=="N" and b3["text"]=="T") or (b8["text"]=="O" and b7["text"]=="H") or (b5["text"]=="A" and b1["text"]=="A") :
        messagebox.showinfo("Warning","Your chances over ,check result")
   
def infP01(b10):
    messagebox.showinfo("Mendez_120980","A Word Guess Game Using Python's GUI.")
    
        
def Showresult(b11):
    def check(event):
            name=entry.get()
            if b1["text"]=="M" and b2["text"]=="A" and b3["text"]=="P" :  #MAP
                                              messagebox.showinfo("Result","You win : "+name)
            elif b4["text"]=="W" and b5["text"]=="I" and b6["text"]=="N" : #WIN
                                              messagebox.showinfo("Result","You win : "+name)
            elif b7["text"]=="B" and b8["text"]=="O" and b9["text"]=="X" : #BOX
                                              messagebox.showinfo("Result","You win : "+name)
            else:
               messagebox.showinfo("Result","Try Again You loose : "+name)

            gui1.destroy()
    gui1=tkinter.Tk()
    gui1.geometry("250x100")
    Label(gui1,text="Enter Your Name",fg="white",bg="black").pack()
    lab=Label(gui1,text="")
    lab.pack()
    entry=Entry(gui1)
    entry.bind("<Return>",check)
    entry.pack()
    lab=Label(gui1,text="")
    lab.pack()
    lab=Label(gui1,text=" Thanks for Playing The Game, Have Fun!! ")
    lab.pack()

    gui1.mainloop()
    
        
def reset(b12):
    b1["text"]=" "
    b2["text"]=" "
    b3["text"]=" "
    b4["text"]=" "
    b5["text"]=" "
    b6["text"]=" "
    b7["text"]=" "
    b8["text"]=" "
    b9["text"]=" "
    

gui=tkinter.Tk()
gui.title("Word Guess")
b1=Button(gui,text=" ",width=10,height=5,font="Arial 10 bold",command=lambda:buttonpress1(b1))
b1.grid(row=0,column=0)
b2=Button(gui,text=" ",width=10,height=5,font="Arial 10 bold",command=lambda:buttonpress2(b2))
b2.grid(row=0,column=1)
b3=Button(gui,text=" ",width=10,height=5,font="Arial 10 bold",command=lambda:buttonpress3(b3))
b3.grid(row=0,column=2)
b4=Button(gui,text=" ",width=10,height=5,font="Arial 10 bold",command=lambda:buttonpress4(b4))
b4.grid(row=1,column=0)
b5=Button(gui,text=" ",width=10,height=5,font="Arial 10 bold",command=lambda:buttonpress5(b5))
b5.grid(row=1,column=1)
b6=Button(gui,text=" ",width=10,height=5,font="Arial 10 bold",command=lambda:buttonpress6(b6))
b6.grid(row=1,column=2)
b7=Button(gui,text=" ",width=10,height=5,font="Arial 10 bold",command=lambda:buttonpress7(b7))
b7.grid(row=2,column=0)
b8=Button(gui,text=" ",width=10,height=5,font="Arial 10 bold",command=lambda:buttonpress8(b8))
b8.grid(row=2,column=1)
b9=Button(gui,text=" ",width=10,height=5,font="Arial 10 bold",command=lambda:buttonpress9(b9))
b9.grid(row=2,column=2)
b10=Button(gui,text="Inf.P01",width=10,height=5,bg="black",fg="white",font="Arial 10 bold",command=lambda:infP01(b10))
b10.grid(row=3,column=0)
b12=Button(gui,text="Reset",width=10,height=5,bg="yellow",fg="red",font="Arial 10 bold",command=lambda:reset(b12))
b12.grid(row=3,column=2)
b11=Button(gui,text="Result",width=10,height=5,bg="orange",fg="black",font="Arial 10 bold",command=lambda:Showresult(b11))
b11.grid(row=0,column=3)
b13=Button(gui,text="Quit",width=10,height=5,bg="red",fg="black",font="Arial 10 bold",command=lambda:play(b13))
b13.grid(row=1,column=3)

L1=Label(gui,text="Word Guess",fg="white",bg="red",font="Arial 10 bold").grid(row=3,column=1)
L1=Label(gui,text="Just 3 Words",width=10,height=5,fg="white",bg="blue",font="Arial 10 bold").grid(row=3,column=3)
L1=Label(gui,text="Guess it",width=10,height=5,fg="black",bg="white",font="Arial 10 bold").grid(row=2,column=3)

def play(b13):
        gui.destroy()   
       
gui.mainloop()
