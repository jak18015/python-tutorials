# Package
from tkinter import *

# Create the window
window=Tk()

# Title the window
window.title("BookStore")

# Title entry
l1=Label(window,text="Title")
l1.grid(row=0,column=0)
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

# Author entry
l2=Label(window,text="Author")
l2.grid(row=1,column=0)
author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=1,column=1)

# Year entry
l3=Label(window,text="Year")
l3.grid(row=0,column=2)
year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=0,column=3)

#ISBN entry
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)
isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

# Listbox
list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

# Scrollbar
sb1=Scrollbar(window)
sb1.grid(row=)

window.mainloop()
