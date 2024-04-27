# Package
from tkinter import *
import backend

# functions
## view button
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

## search button
def search_command(title_text="",author_text="",year_text="",isbn_text=""):
    list1.delete(0,END)
    for row in backend.search(title_text, ):
        list1.insert(END,row)
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
sb1.grid(row=2,column=2,rowspan=6)

# Configure method
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# View all button
b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)

# Search button
b2=Button(window,text="Search",width=12,command=search_command)
b2.grid(row=3,column=3)

# Add button
b3=Button(window,text="Add",width=12)
b3.grid(row=4,column=3)

#  Update button
b3=Button(window,text=" Update",width=12)
b3.grid(row=5,column=3)

#  Delete button
b5=Button(window,text=" Delete",width=12)
b5.grid(row=5,column=3)

# Close button
b6=Button(window,text="Close",width=12)
b6.grid(row=6,column=3)

window.mainloop()
