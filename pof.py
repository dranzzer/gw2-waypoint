from tkinter import *
import requests
import json
import pyperclip as pc
import pprint as pp
pof_result = requests.get("https://api.guildwars2.com/v2/continents/1/floors?ids=49")
pof_result.status_code
pof_result_json = pof_result.json()
pof_wp_db = []


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
                                    pof_wp_db.append(i)


pp.pprint(pof_wp_db)
print(type(pof_wp_db))

for each in pof_wp_db:
    for x,y in each.items():
        if "waypoint" in str(y).lower():
            print(y)
            print(each.get("chat_link"))
