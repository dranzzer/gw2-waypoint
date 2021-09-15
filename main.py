from tkinter import *
import requests
import json
import pyperclip as pc
result = requests.get("https://api.guildwars2.com/v2/continents/1/floors?ids=1")
result.status_code
result_json = result.json()
wp_db = []


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







win=Tk()

win.title("test")

def update(data):
	#clear listbox
	listbox.delete(0,END)
	listbox.pack_forget()
	#add toppings to list box
	if entry.get() == "":
		data=[]
	
	else:
		for item in data:
			listbox.pack(fill=BOTH)		
			listbox.insert(END,item.get("name"))

#change entry to listbox that was clicked
def fillout(e):
	#delete whatever is in entrybox

	entry.delete(0,END)
	#add clicked item to entry box
	entry.insert(0,listbox.get(ANCHOR))

	for each in wp_db:
		if each.get("name") == listbox.get(ANCHOR):
			pc.copy(each.get("chat_link"))
#check entry vs listbox
def check(e):
	typed = entry.get()
	if typed =='':
		data=[]
		listbox.pack_forget()

	else:
		data=[]
		listbox.pack(fill=BOTH)
		for item in wp_db:
			if typed.lower() in item.get("name").lower():
				data.append(item)
	update(data)



entry = Entry(win,width=30)
entry.pack(fill=X)

listbox = Listbox(win)
listbox.pack(fill=BOTH)




update(wp_db)
#update entry box

listbox.bind("<<ListboxSelect>>",fillout)

entry.bind("<KeyRelease>",check)


win.mainloop()