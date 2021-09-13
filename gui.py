
# Python program demonstrating
# ScrolledText widget in tkinter
  
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *
  
# Creating tkinter main window
win = tk.Tk()
win.title("ScrolledText Widget")
  
# Title Label

  
def reply(name):
    print(name)





Label(win, text="search:").pack(side=TOP)
ent = Entry(win)
ent.bind("<Return>", (lambda event: reply(ent.get())))
ent.pack(side=TOP)
btn = Button(win,text="Submit", command=(lambda: reply(ent.get())))
btn.pack(side=LEFT)


# Creating scrolled text 
# area widget
text_area = scrolledtext.ScrolledText(win, 
                                      wrap = tk.WORD, 
                                      width = 40, 
                                      height = 10, 
                                      font = ("Times New Roman",
                                              15))
test_list = ["apple", "banana", "cherry"]           


text_area.insert('end',test_list)
text_area.pack()
  
# Placing cursor in the text area
text_area.focus()
win.mainloop()

