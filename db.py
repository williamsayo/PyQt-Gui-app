import sqlite3
import os

cwd = os.path.split(__file__)[0]
conn = sqlite3.Connection(os.path.join(cwd,'users.sqlite3'))
cur = conn.cursor()

cur.execute("""CREATE TABLE users (id integer primary key,
    first_name varchar(20),"
    last_name varchar(20),
    username varchar(20),
    email varchar(50),
    password varchar(25))""")

cur.close()

conn.close()