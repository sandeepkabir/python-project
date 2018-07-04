#Q1




import sys
import tkinter
from tkinter import *

def display():
	print("Hello World!")
	sys.exit()
root = Tk()
b=Button(root, text="EXIT", command=display)
b.pack()
root.mainloop()


#Q2



import tkinter
from tkinter import *

def display():
	print("Hello World!")
	
root=Tk()
b=Button(root,text="click",width=25,bg='blue',fg='white',command=display)
b.pack()
root.mainloop()


		   
#Q3




import tkinter
from tkinter import *
import sys
def Change():
	label.config(text= "JUICE")
root = Tk()
label = Label(root,text="hello ")
label.grid(row = 0)
btn = Button(root, text="Change",command=Change)
btn.grid(row= 1)
btn2 = Button(root, text="Exit",command=sys.exit)
btn2.grid(row= 2)
root.mainloop()


#Q4



import tkinter
from tkinter import *

def show():
	print(entry.get())
	
root=Tk()
root.title("My App")
root.geometry("250x250")
root.resizable(True,True)
root.minsize(200,200)
entry=Entry(root,width=20)
entry.pack()
b=Button(root,text='click',width=20,command=show)
b.pack()
root.mainloop()

