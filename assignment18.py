#Q1




import tkinter
from tkinter import *
d={'sandeep':6316229,'harkirat':447656,'gfjdgc':6316235,'cncyh':,'dqd':6316230,'Rkmcj':456789,'Vi':6316234,'utdyd':456789,'jygffy':6316234}
root=Tk()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,yscrollcommand=s.set)
for line in d:
    l.insert(END,'this is ' +str(line))
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())
root.mainloop()
		   
		   
#Q2



import tkinter
from tkinter import *

root=Tk()

def show():
    a=entry.get()
    b=entry1.get()
    mylist.insert(END,a)
    dict[a]=b
    print(dict)

name=False
Mobile=False

def name(event):
    entry.delete(0,END)
    name=True

def Mobile(event):
    entry1.delete(0,END)
    Mobile=True

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
d={'sandeep':6316229,'harkirat':447656,'gfjdgc':6316235,'cncyh':,'dqd':6316230,'Rkmcj':456789,'Vi':6316234,'utdyd':456789,'jygffy':6316234}
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for i in d:
    mylist.insert(END,i)
mylist.pack(fill=BOTH)


entry=Entry(root)
entry.insert(0,'name')
entry.bind("<Button>",name)
entry.pack()

entry1=Entry(root)
entry1.insert(0,'Mobile No.')
entry1.bind("<Button>",Mobile)
entry1.pack()


b=Button(root,text='Submit',command=show)
b.pack()

Scrollbar(mylist,orient="vertical")
scrollbar.config(command=mylist.yview)

#OR

scrollbar['command']=mylist.yview
root.geometry("100x100")
root.minsize(50,50)
root.maxsize(250,250)
root.mainloop()
