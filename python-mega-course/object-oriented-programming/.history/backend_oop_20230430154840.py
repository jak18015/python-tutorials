# package
import sqlite3

class Database:

    #connect to the table, and create one if one doesn't exist
    def __init__():
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        conn.commit()
        conn.close()

    # insert a new book
    def insert(title,author,year,isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)",(title,author,year,isbn))
        conn.commit()
        conn.close()

    # view books
    def view():
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM book")
        rows=cur.fetchall()
        conn.close()    
        return rows

    # search for a book using any one or multiple of the queries
    ## the empty strings for the arguments allow for individual searches to not return an error
    def search(title="",author="",year="",isbn=""):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows=cur.fetchall()
        conn.close()    
        return rows

    # delete a book
    def delete(id):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (id,))
        conn.commit()
        conn.close()    

    # update database
    def update(id,title,author,year,isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        conn.commit()
        conn.close()    



# insert("The Sun", "John Smith", 1943, 39399348439)
# print(search(author="John Smith"))
# delete(4)
# update(1, "Not My Life", "John Quincy Adams", 1945, 393993483)
# print(view())
