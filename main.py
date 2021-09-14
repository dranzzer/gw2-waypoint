
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

  
def search(search):
    for q1,q2 in test_list.items():
        if search.lower() in q1.lower():
            print("Key: " +q1)
            print("Value: " +q2)





Label(win, text="search:").pack(side=TOP)
ent = Entry(win)
ent.bind("<Return>", (lambda event: search(ent.get())))
ent.pack(side=TOP)
btn = Button(win,text="Submit", command=(lambda: search(ent.get())))
btn.pack(side=LEFT)


# Creating scrolled text 
# area widget
text_area = scrolledtext.ScrolledText(win, 
                                      wrap = tk.WORD, 
                                      width = 40, 
                                      height = 10, 
                                      font = ("Times New Roman",
                                              15))
test_list = {"Sam": "Blue", "Amy": "Red", "Sarah": "Yellow"}

text_area.insert('end',test_list)
text_area.pack()
  
# Placing cursor in the text area
text_area.focus()
win.mainloop()

