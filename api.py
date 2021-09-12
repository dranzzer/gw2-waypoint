import requests
result = requests.get("https://api.guildwars2.com/v2/continents/1/floors?ids=1")



result.status_code

result_json = result.json()

#print(result_json[0]["regions"]["1"]["maps"]["26"]["points_of_interest"])

#pulling from api
waypoint_pull =result_json[0]["regions"]["1"]["maps"]["26"]["points_of_interest"]
for k, v in waypoint_pull.items():
    for a,s in v.items():
        if s == "waypoint":
            print(v)