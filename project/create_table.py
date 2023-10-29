import sqlite3, csv
import pandas as pd
#Creating the SQL Statement to create the table

import re

def string_aufteilen(text):
    pattern = r'(\d+|%)+'
    result = re.sub('%', '_percent', text)
    result = re.sub('\+', '_and_', result)
    result = re.sub('/', '_per_', result)
    result = re.sub(pattern, lambda match: '"' + match.group(0) + '"', result)
    return result


conn = sqlite3.connect('Scouting.db')
cur=conn.cursor()

sql="Create Table Players ("

#executing create Statement for Players
with open('21_22_Players.csv', 'r') as file:
    for row in file:
        B=row.split(";")
        for i in range(len(B)):

            if i==0:
                sql+=B[i]+" Numeric,"
            elif i<6:
                sql+=B[i]+" TEXT,"
            elif i==len(B)-1:
                sql+=B[i]+" Numeric)"
            else:
                sql+=B[i]+" Numeric,"
        break
sql=string_aufteilen(sql)

cur.execute(sql)

conn.commit()
cur.close()
conn.close()

 