import sqlite3
import psycopg2

# steps for working with databases
## connect to database
## create a cursor object
## apply sql query
## commit changes to database
## close database connection



def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?)")
    conn.commit()
    conn.close()
