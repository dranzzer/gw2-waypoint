#import tkinter as tk
import pyperclip as pc

#window = tk.Tk()



auric_basin_wp = {
    "chak hollow waypoint" : "[&BEkIAAA=]",
    "eastwatch waypoint" : "[&BGwIAAA=]",
    "northwatch waypoint" : "[&BN0HAAA=]",
    "southwatch waypoint" : "[&BAIIAAA=]",
    "forgotten city  waypoint" : "[&BMYHAAA=]",
    "wanderer's waypoint" : "[&BNYHAAA=]",
    "westwatch waypoint" : "[&BAYIAAA=]"
}

search = input("Enter waypoint here")

for wp_name,wp_code in auric_basin_wp.items():
    if search in wp_name:
        print(wp_name , wp_code)
        pc.copy(wp_code)
    

#test
#window.mainloop()

