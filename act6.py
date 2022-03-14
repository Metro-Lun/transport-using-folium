import folium
import sqlite3

def creation_carte(liste) :
    carte = folium.Map(location = (45.750982, 4.827891), zoom_start = 11, attr = "© Contributeurs OpenStreetMap")

    for i in range(1, len(liste)) :        # ajouter chacun son tour les événements de la liste fournie
        
        if liste[i][2] in {"A","B","C","D","F1","F2","F1 & F2","T1","T2","T3","T4","T5","T6","T7","T3 & T7","T3 & T4","T2 & T5","T1 & T2","T1 & T4","T1 & T6"} :
            icon = "subway"
        else :                  # on garde les jolies icônes
            icon = "bus"
        
        if liste[i][-1] == "True" :     # couleurs représentant la situation géographique de la commune et des arrêts
            if liste[i][11] in {"LYON","VILLEURBANNE","LYON 1ER","LYON 2EME","LYON 3EME","LYON 4EME","LYON 5EME","LYON 6EME","LYON 7EME","LYON 8EME","LYON 9EME"} :
                c = "red"   # = arrêt situé à Lyon ou Villeurbanne
            else :
                c = "blue"  # = arrêt situé ni à Lyon ni à Villeurbanne mais dans la Métropole
        else :
            c = "green"     # = le reste.

        folium.Marker(
            location = [liste[i][7], liste[i][8]],
            popup = f"{liste[i][1]} ({liste[i][2]})",
            icon = folium.Icon(color = c, icon = icon, prefix = "fa"),
        ).add_to(carte)

    carte.save("act6_tcl2.html")

# Jointure des deux tables -> création d'une liste complète
connexion = sqlite3.connect("jointure.sqlite3")   
c = connexion.cursor()                                      
table = c.execute("SELECT * FROM Arrets JOIN Communes ON Arrets.commune_gid = Communes.gid").fetchall()

creation_carte(table)