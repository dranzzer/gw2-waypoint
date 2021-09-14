import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *
import requests
import json
result = requests.get("https://api.guildwars2.com/v2/continents/1/floors?ids=1")
result.status_code
result_json = result.json()
wp_db = []
  
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


              

wp_pull = result_json[0]["regions"]
for region_id,region in wp_pull.items():
    for a,b in region.items():
        if a =="maps":
            for c,v in b.items():
                for f,g in v.items():
                    if f=="points_of_interest":
                        for u,i in g.items():
                            for q1,q2 in i.items():
                                if q2=="waypoint":
                                    wp_db.append(i)




# Placing cursor in the text area
text_area.focus()
win.mainloop()














