import sqlite3, csv
import pandas as pd

conn = sqlite3.connect('Scouting.db')
cur=conn.cursor()

with open('21_22_Players.csv', 'r') as file:
    for row in file:
        B=row.split(";")

        break

s=""
for i in range(len(B)-1):
    s+="?,"
s+="?"

#Inserting the Data into the Table from CSV
with open('21_22_Players.csv', 'r') as file:

    for row in file:

        cur.execute("INSERT INTO Players VALUES ({})".format(s), row.split(";") )
        conn.commit()

cur.close()
conn.close()