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
screen_height = win.winfo_screenheight()
print(type(screen_height))
x=0
y=screen_height * 0.0240740740740741

win.geometry('+%d+%d'%(x,y)) 

def update(data):
	#clear listbox
	listbox.delete(0,END)
	listbox.grid_forget()
	#add toppings to list box
	if entry.get() == "":
		data=[]
	
	else:
		for item in data:
			listbox.grid(row=1,column=0,columnspan=2,sticky=EW)
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
		listbox.grid_forget()

	else:
		data=[]
		listbox.grid(row=1,column=0,columnspan=2,sticky=EW)
		for item in wp_db:
			if typed.lower() in item.get("name").lower():
				data.append(item)
	update(data)



entry = Entry(win,width=30,bd=0,bg="black",fg="white",relief=RIDGE)
entry.grid(row=0,column=0,sticky=NSEW)



kill_button =Button(win,text=" X ",bd=1,bg="black",fg="white",relief=RIDGE,command=win.destroy)
kill_button.grid(row=0,column=1,sticky=EW)

listbox = Listbox(win,bd=1,bg="black",fg="white",relief=RIDGE)
listbox.grid(row=1,column=0,columnspan=2,sticky=EW)




update(wp_db)
#update entry box

listbox.bind("<<ListboxSelect>>",fillout)

entry.bind("<KeyRelease>",check)


win.overrideredirect(True)
win.attributes('-topmost',True)
win.mainloop()