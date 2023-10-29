import sqlite3
import pandas as pd

cnx=sqlite3.connect(C:\Users\nikla\java_beginners\end_project.\database.sqlite")
df = pd.read_sql_query("SELECT * FROM Player", cnx)