from tkinter import *
import requests
import json
import pyperclip as pc
import pprint as pp
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


#POF WP Database Pull
pof_result = requests.get("https://api.guildwars2.com/v2/continents/1/floors?ids=49")
pof_result.status_code
pof_result_json = pof_result.json()


pof_wp_pull = pof_result_json[0]["regions"]
for region_id,region in pof_wp_pull.items():
    for a,b in region.items():
        if a =="maps":
            for c,v in b.items():
                for f,g in v.items():
                    if f=="points_of_interest":
                        for u,i in g.items():
                            for q1,q2 in i.items():
                                if q2=="waypoint":
                                    wp_db.append(i)




#custom DB handle where future user configs will be appended to 



wp_db.extend([{'chat_link': '[&BGwIAAA=]','name': 'Auric Basin - East /AB/octovine','type': 'waypoint'}
	,{'chat_link': '[&BAYIAAA=]','name': 'Auric Basin - West /AB/octovine','type': 'waypoint'}
	,{'chat_link': '[&BN0HAAA=]','name': 'Auric Basin - North /AB/octovine','type': 'waypoint'}
	,{'chat_link': '[&BAIIAAA=]','name': 'Auric Basin - South /AB/octovine','type': 'waypoint'}
	,{'chat_link': '[&BPUHAAA=]','name': 'Tangled Depths Chak Gerent /TD','type': 'waypoint'}
	,{'chat_link': '[&BNABAAA=]','name': 'Tequatl - Splintered Coast - Sparkfly Fen','type': 'waypoint'}
	,{'chat_link': '[&BKoBAAA=]','name': 'Triple Trouble (TT) Bloodtide Coast','type': 'waypoint'}
	,{'chat_link': '[&BAkMAAA=]','name': 'Dragonstorm - Twisted Marionette - EOTN - DS','type': 'waypoint'}
	,{'chat_link': '[&BIABAAA=]','name': 'Plains of Ashford - Smokestead Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BPIAAAA=]','name': 'Queensdale - Crossing Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BDQBAAA=]','name': 'Caledon Forest - Astorea Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BEAAAAA=]','name': 'Metrica Province - Soren Draa Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BHMBAAA=]','name': "Wayfarer Foothills - Hero's Moot Waypoint",'type': 'waypoint'}
	,{'chat_link': '[&BEIEAAA=]','name': 'Diessa Plateau - Blackblade Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BBIAAAA=]','name': 'Kessex Hills - Cereboth Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BGEAAAA=]','name': 'Brisban Wildlands - Brilitine Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BLYAAAA=]','name': "Snowden Drifts - Lost Child's Sorrow Waypoint",'type': 'waypoint'}
	,{'chat_link': '[&BJQBAAA=]','name': 'Gendarran Fields - Almuten Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BOYAAAA=]','name': "Lornar's Pass - Demon's Maw Waypoint",'type': 'waypoint'}
	,{'chat_link': '[&BEwBAAA=]','name': 'Fields of Ruin - Fangfury Watch Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BMMAAAA=]','name': 'Harathi Hinterlands - Arcallion Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BP0BAAA=]','name': 'Blazeridge Steppes - Behem Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BFcCAAA=]','name': 'Dredgehaunt Cliffs - Frostland Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BKMBAAA=]','name': 'Bloodtide Coast - Archen Foreland Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BOYBAAA=]','name': 'Iron Marches - Hellion Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BFMCAAA=]','name': 'Timberline Falls - Iron Veil Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BMYBAAA=]','name': "Sparkfly Fen - Braggi's Stead Waypoint",'type': 'waypoint'}
	,{'chat_link': '[&BBcCAAA=]','name': 'Fireheart Rise - Pig Iron Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BMwCAAA=]','name': "Mount Maelstrom - Bard's Waypoint",'type': 'waypoint'}
	,{'chat_link': '[&BOwCAAA=]','name': 'Straits of Devastation - Bramble Pass Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BHgCAAA=]','name': 'Frostgorge Sound - Arundon Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BK4CAAA=]','name': "Malchor's Leap - Blighted Arch Waypoint",'type': 'waypoint'}
	,{'chat_link': '[&BCIDAAA=]','name': 'Cursed Shore - Murdered Dreams Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BLQEAAA=]','name': 'Rata Sum - Magicat Court Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BKcDAAA=]','name': 'Black Citadel - Factorium Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BCoDAAA=]','name': "Divinity's Reach - Commons Waypoint",'type': 'waypoint'}
	,{'chat_link': '[&BIkDAAA=]','name': 'Hoelbrak - Bear Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BBIEAAA=]','name': 'The Grove - Caledon Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BH8HAAA=]','name': 'The Silverwastes - Camp Resolve Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BJcHAAA=]','name': 'Dry Top - Repair Station Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BN4HAAA=]','name': 'Verdant Brink - Shipwreck Peak Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BBAIAAA=]','name': "Dragon's Stand - Pact Base Camp Waypoint",'type': 'waypoint'}
	,{'chat_link': '[&BEEJAAA=]','name': 'Bloodstone Fen - Ground Zero Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BGAJAAA=]','name': 'Ember Bay - Crumbling Trail Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BIEJAAA=]','name': "Bitterfrost Frontier - Koda's Welcome Waypoint",'type': 'waypoint'}
	,{'chat_link': '[&BK0JAAA=]','name': "Lake Doric - Doric's Landing Waypoint",'type': 'waypoint'}
	,{'chat_link': '[&BNUJAAA=]','name': 'Draconis Mons - Ancient Hollow Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BO8JAAA=]','name': "Siren's Landing - Camp Reclamation Waypoint",'type': 'waypoint'}
	,{'chat_link': '[&BLsKAAA=]','name': 'Crystal Oasis - Amnoon Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BGsKAAA=]','name': 'Desert Highlands - Makali Outpost Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BFMKAAA=]','name': "Elon Riverlands - Augury's Shadow Waypoint",'type': 'waypoint'}
	,{'chat_link': '[&BNwKAAA=]','name': 'The Desolation - Bonestrand Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BKUKAAA=]','name': 'Domain of Vabbi - Cragged Vale Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BAkLAAA=]','name': 'Domain of Istan - Chalon Docks Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BEMLAAA=]','name': 'Sandswept Isles - Atholma Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BFcLAAA=]','name': 'Domain of Kourna - Allied Encampment Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BJkLAAA=]','name': 'Jahai Bluffs - Reclaimed Chantry Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BLkLAAA=]','name': 'Thunderhead Peaks - Observation Deck Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BN4LAAA=]','name': 'Dragonfall - Pact Command Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BA4MAAA=]','name': 'Grothmar Valley - Dalada Forest Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BDkMAAA=]','name': 'Bjora Marches - Still Waters Speaking Waypoint','type': 'waypoint'}
	,{'chat_link': '[&BGQMAAA=]','name': 'Drizzlewood Coast - Base Camp Waypoint','type': 'waypoint'}
	])









win=Tk()

win.title("gw2-waypoint")
screen_height = win.winfo_screenheight()
win.iconbitmap("D:/Documents/GitHub/gw2-waypoint/icon.ico")
x=5
y=screen_height * 0.0240740740740741

win.geometry('+%d+%d'%(x,y)) 

def update(data):
	#clear listbox
	listbox.delete(0,END)
	listbox.grid_forget()
	#add toppings to list box
	if entry.get() == "":
		data=[]
		#listbox.grid_forget()
	
	else:
		for item in data:
			listbox.grid(row=1,column=0,columnspan=3,sticky=EW)
			listbox.insert(END,item.get("name"))

#change entry to listbox that was clicked
def fillout(e):
	#delete whatever is in entrybox

	entry.delete(0,END)
	#add clicked item to entry box
	#entry.insert(0,listbox.get(ANCHOR))

	for each in wp_db:
		if each.get("name") == listbox.get(ANCHOR):
			pc.copy(each.get("chat_link"))

	listbox.delete(0,END)
	listbox.grid_forget()

#check entry vs listbox
def check(e):
	typed = entry.get()
	
	if typed =='':
		data=[]

		#listbox.grid_forget()

	else:
		data=[]
		listbox.grid(row=1,column=0,columnspan=3,sticky=EW)
		i=1	
		for item in wp_db:
			if typed.lower() in item.get("name").lower():
				data.append(item)
				i+=1
				if i==8:
					break
	update(data)
	entry.focus_set()


#minimise window 
def minimise_button():
	win.overrideredirect(0)
	win.iconify()



#maximise window

def max_window(event):
	win.overrideredirect(1)
	win.attributes('-topmost',True)


	
entry = Entry(win,width=30,bd=0,bg="black",fg="white",relief=RIDGE,insertbackground="white")
entry.grid(row=0,column=0,sticky=NSEW)

minimise_button = Button(win,text=" - ",bd=1,bg="black",fg="white",relief=RIDGE,command=minimise_button)
minimise_button.grid(row=0,column=1,sticky=EW)
minimise_button.bind("<Map>",max_window)
kill_button =Button(win,text=" X ",bd=1,bg="black",fg="white",relief=RIDGE,command=win.destroy)
kill_button.grid(row=0,column=2,sticky=EW)

listbox = Listbox(win,bd=1,bg="black",fg="white",relief=RIDGE)
listbox.grid(row=1,column=0,columnspan=3,sticky=EW)




update(wp_db)
#update entry box

listbox.bind("<<ListboxSelect>>",fillout)
entry.bind("<KeyRelease>",check)









win.overrideredirect(True)
win.attributes('-topmost',True)


win.wm_attributes('-alpha', 0.7)


pp.pprint(listbox.get(ANCHOR))





win.mainloop()