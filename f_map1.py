import csv
import folium

def create_map(L) :
    new_map = folium.Map(location = (45.750982, 4.827891), zoom_start = 11, attr = "© OpenStreetMap contributors")

    for i in range(1, len(L)) :
        
        if L[i][2] == "A" :     # in order to give the lines their colors according to the city's map
            c = "pink"
            icon = "subway"
        elif L[i][2] == "B" :
            c = "blue"
            icon = "subway"
        elif L[i][2] == "C" :
            c = "orange"
            icon = "subway"
        elif L[i][2] == "D" :
            c = "darkgreen"
            icon = "subway"
        elif L[i][2] in {"F1", "F2", "F1 & F2"} :
            c = "green"
            icon = "subway"
        elif L[i][2] in {"T1", "T2", "T3", "T4", "T5", "T6", "T7", "T3 & T7", "T3 & T4", "T2 & T5", "T1 & T2", "T1 & T4", "T1 & T6"} :
            c = "purple"
            icon = "subway"     # no tram icon ?
        else :
            c = "red"
            icon = "bus"
        
        folium.Marker(
            location = [L[i][7], L[i][8]],    
            popup = f"{L[i][1]} ({L[i][2]})",   # displays the name and the service (lines)
            icon = folium.Icon(color = c, icon = icon, prefix = "fa"),
        ).add_to(new_map)

    new_map.save("map1.html")

with open('stops.csv', newline='') as file:
    read = csv.reader(file, delimiter=',')
    table = list(read)

for i in range(1, len(table)):
    table[i][7] = float(table[i][7])    # coordinates, from str to float
    table[i][8] = float(table[i][8])

create_map(table)