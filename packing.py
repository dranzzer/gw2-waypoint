from tkinter import *

root = Tk()


button1 = Entry(root,width=30)
button1.grid(row=0,column=0,sticky=NSEW)

button2 = Button(text="x")
button2.grid(row=0,column=1,sticky=EW)

button3 = Button(text="listbox")
button3.grid(row=1,column=0,columnspan=2,sticky=EW)






root.mainloop()