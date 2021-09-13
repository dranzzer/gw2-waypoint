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

wp_pull =result_json[0]["regions"]["1"]["maps"]
for map_number,map_data in wp_pull.items():
    for name,min_level in map_data.items():
        if name =="points_of_interest":
            for x,c in min_level.items():
                for q,w in c.items():
                    if w=="waypoint":
                        wp_db.append(c)                


#print(len(wp_db))


with open('output.json','w') as fs:
    json.dump(wp_db,fs,indent=4)