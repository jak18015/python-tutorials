from tkinter import *

window = Tk()

b1=Button(window,text="Execute")
b1.grid(row=0,column=0)

e1=Entry(window,text="Put Your Text Here")
e1.grid(row=0,column=1)

t1=Text(window)
t1.grid(row=0,column=2)




window.mainloop()