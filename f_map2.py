import folium
import sqlite3

def create_map(L) :
    new_map = folium.Map(location = (45.750982, 4.827891), zoom_start = 11, attr = "© .OpenStreetMap contributors")

    for i in range(1, len(L)) :
        
        if L[i][2] in {"A","B","C","D","F1","F2","F1 & F2","T1","T2","T3","T4","T5","T6","T7","T3 & T7","T3 & T4","T2 & T5","T1 & T2","T1 & T4","T1 & T6"} :
            icon = "subway"
        else :
            icon = "bus"
        
        if L[i][-1] == "True" :
            if L[i][11] in {"LYON","VILLEURBANNE","LYON 1ER","LYON 2EME","LYON 3EME","LYON 4EME","LYON 5EME","LYON 6EME","LYON 7EME","LYON 8EME","LYON 9EME"} :
                c = "red"   # = this stop is located in the main cities
            else :
                c = "blue"  # = this stop is located in the outskirts of the agglomeration
        else :
            c = "green"     # = this stop is located further than the outskirts

        folium.Marker(
            location = [L[i][7], L[i][8]],
            popup = f"{L[i][1]} ({L[i][2]})",
            icon = folium.Icon(color = c, icon = icon, prefix = "fa"),
        ).add_to(new_map)

    new_map.save("map2.html")

# needed to join my tables to get all my stops
connection = sqlite3.connect("joined.sqlite3")   
c = connection.cursor()                                      
table = c.execute("SELECT * FROM Stops JOIN Towns ON Stops.id_town = Towns.id").fetchall()

create_map(table)