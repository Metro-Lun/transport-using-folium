import csv
import folium

def creation_carte(liste) :
    carte = folium.Map(location = (45.750982, 4.827891), zoom_start = 11, attr = "© Contributeurs OpenStreetMap")

    for i in range(1, len(liste)) :        # ajouter chacun son tour les événements de la liste fournie
        
        if liste[i][2] == "A" :     # pour donner leur couleur aux lignes !
            c = "pink"
            icon = "subway"
        elif liste[i][2] == "B" :
            c = "blue"
            icon = "subway"
        elif liste[i][2] == "C" :
            c = "orange"
            icon = "subway"
        elif liste[i][2] == "D" :
            c = "darkgreen"
            icon = "subway"
        elif liste[i][2] in {"F1", "F2", "F1 & F2"} :
            c = "green"
            icon = "subway"
        elif liste[i][2] in {"T1", "T2", "T3", "T4", "T5", "T6", "T7", "T3 & T7", "T3 & T4", "T2 & T5", "T1 & T2", "T1 & T4", "T1 & T6"} :
            c = "purple"
            icon = "subway"     # malheureusement, pas d'icône tramway...
        else :
            c = "red"
            icon = "bus"
        
        folium.Marker(
            location = [liste[i][7], liste[i][8]],      # attributs coordinates0 et coordinates1
            popup = f"{liste[i][1]} ({liste[i][2]})",
            icon = folium.Icon(color = c, icon = icon, prefix = "fa"),
        ).add_to(carte)

    carte.save("act5_tcl.html")

with open('arrets.csv', newline='') as fichier:
    lecture = csv.reader(fichier, delimiter=',')
    table = list(lecture)

for i in range(1, len(table)):
    table[i][7] = float(table[i][7])    # pour passer des strings dûs à la lecture du fichier...
    table[i][8] = float(table[i][8])    # ... à des flottants (pour les coordonnées)

creation_carte(table)   # Laissons la magie opérer...