import folium

# Création de l'objet carte
def creation_carte(liste) :
    carte = folium.Map(location = (46.396,2.505), zoom_start = 7, attr = "© Contributeurs OpenStreetMap")

    folium.Marker(      # marqueur placé au centre de la carte
        location = (46.396,2.505),
        popup = "Un coin un peu paumé",
        icon = folium.Icon(color = "red", icon = "fire")
    ).add_to(carte)

    for i in range(len(liste)) :        # ajouter chacun son tour les événements de la liste fournie
        folium.Marker(
            location = [liste[i][1],liste[i][2]],
            popup = liste[i][0],
            icon = folium.Icon(icon = "info-sign"),
        ).add_to(carte)

    carte.save("act5_exemple.html")
        
eves = [
('eve1', 44.29, 2.519),
('eve2', 44.339, 2.105),
('eve3', 43.855, 2.838),
('eve4', 44.332, 2.787),
('eve5', 44.126, 3.253),
('eve6', 44.484, 2.496),
('eve7', 44.316, 2.585),
('eve8', 43.849, 2.899),
('eve9', 44.366, 2.04199),
('eve10', 43.933, 2.664)
]

# Appel de la fonction, création de la carte
creation_carte(eves)
