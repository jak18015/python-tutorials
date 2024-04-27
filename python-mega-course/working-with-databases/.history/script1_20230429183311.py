import sqlite3
import psycopg2


# steps for working with databases
## connect to database
## create a cursor object
## apply sql query
## commit changes to database
## close database connection

conn=qlite3.connect("lite.db")