import requests
import json
result = requests.get("https://api.guildwars2.com/v2/continents/1/floors?ids=1")



result.status_code

result_json = result.json()


wp_db = []

#print(result_json[0]["regions"]["1"]["maps"]["26"]["points_of_interest"])

#pulling from api
#waypoint_pull =result_json[0]["regions"]["1"]["maps"]["26"]["points_of_interest"]
#for k, v in waypoint_pull.items():
#    for a,s in v.items():
#        if s == "waypoint":
#           wp_db.append(v)

#wp_pull =result_json[0]["regions"]["1"]["maps"]
#for map_number,map_data in wp_pull.items():
 #   for name,min_level in map_data.items():
  #      if name =="points_of_interest":
   #         for x,c in min_level.items():
    #            for q,w in c.items():
     #               if w=="waypoint":
      #                  wp_db.append(c)                

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


search = input("enter waypoint here")
for each in wp_db:
    
    if search.lower() in each.get("name").lower():
        print(each.get("name"))
        print(each.get("chat_link"))
#print(len(wp_db))
#with open('output.json','w') as fs:
#    json.dump(wp_db,fs,indent=4)