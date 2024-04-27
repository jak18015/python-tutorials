# package
import sqlite3

class Database:

    #connect to the table, and create one if one doesn't exist
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    # insert a new book
    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    # view books
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall() 
        return rows

    # search for a book using any one or multiple of the queries
    ## the empty strings for the arguments allow for individual searches to not return an error
    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows=self.cur.fetchall()    
        return rows

    # delete a book
    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()    

    # update database
    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()    
    
    #close
    def __del__(self):
        self.conn.close()