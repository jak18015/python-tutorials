import psycopg2

# steps for working with databases
## (1) connect to database
## (2) create a cursor object
## (3) apply sql query
## (4) commit changes to database
## (5) close database connection

# create the table
def create_table():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='5432' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

# insert an item with its quantity and price
def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='5432' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

# view the table
def view():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='5432' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

# delete a row
def delete(item):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='5432' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

# update a row
def update(quantity,price,item):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='5432' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity,price,item))
    conn.commit()
    conn.close()


# create_table()
# insert("Orange",10,15)
# delete("Orange")
update(11,5.69,"Water Glass")

print(view())