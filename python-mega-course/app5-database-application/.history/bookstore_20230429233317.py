from tkinter import *

window=Tk()

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=1,column=0)

l3=Label(window,text="Year")
l3.grid(row=0,column=1)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=1)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid()

window.mainloop()
