from tkinter import *

window=Tk()

#Title entry
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=1,column=0)

l3=Label(window,text="Year")
l3.grid(row=0,column=2)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)


author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=1,column=1)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=0,column=3)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)


window.mainloop()
