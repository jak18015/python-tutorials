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
cur.execute("CREATE ")