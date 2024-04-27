import sqlite3
import psycopg2


# steps for working with databases
## connect to database
## create a cursor object
## apply sql query
## commit changes to database
## close database connection

conn=sqlite3.connect("lite.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
cur.execute("INSERT INTO store VALUES ('Wine Glass', 3, )")
conn.commit()
conn.close()