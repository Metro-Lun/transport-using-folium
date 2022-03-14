import sqlite3

connection = sqlite3.connect("requetes.sqlite3")
c = connection.cursor()

c.execute("SELECT * FROM Arrets")

data_list = c.fetchall()	# obtain the results as a list
print(f"1) I've got {len(data_list)} saves in my data base.")