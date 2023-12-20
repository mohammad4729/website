import sqlite3

con = sqlite3.connect("cus.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Customers(
        Id INTEGER PRIMARY KEY,
        Name VARCHAR(200),
        Number VARCHAR(20)
    )
""")



con.commit()
con.close()