# Transportation using Folium
Maps about transportation - just for my pleasure.

## Table of contents
* [Description](#description)
* [Languages and library](#languages-and-library)
* [What do you need to run the project ?](#what-do-you-need-to-run-the-project)
* [How to use this ?](#how-to-use-this)

## Description
The goal of this project was to use an open-source database, based on .csv files from the French government's open-data site, to create HTML files containing maps and markers.

Being a passionate about public transport, I decided to use [this database](https://data.grandlyon.com/jeux-de-donnees/points-arret-reseau-transports-commun-lyonnais/info) representing all metro, tram, funicular, and bus stops located in Lyon, France and its conurbation.

## Languages and libraries
* Python 3.
* Folium / CSV / SQLite3 libraries
* SQL

## What do you need to run the project ?
* A database editor (such as DB Browser for SQLite)

## How to use this ?
The `f_map1.py` file exploits data from the `stops.csv` file
The `f_map2.py` file exploits data from the `joined.sqlite3` database
Run these programs in order to obtain a HTML file containing the map. Soon I'll add a complete web page (HTML + CSS).
