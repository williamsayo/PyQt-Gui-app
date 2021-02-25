from sqlite3.dbapi2 import OperationalError
import sqlite3
import os

cwd = os.path.split(__file__)[0]

media = os.path.join(os.path.split(__file__)[0],"media/profile_pics")
default_img = os.path.join(media,"default1.png")

class Database():
    def __init__(self):
        self.conn = sqlite3.Connection(os.path.join(cwd,'users.sqlite3'))
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.cur = self.conn.cursor()        

    def createUser(self,firstname,lastname,username,email,password):

        self.cur.execute("""CREATE TABLE IF NOT EXISTS users (user_id integer primary key,
            first_name varchar(20),
            last_name varchar(20),
            # username varchar(20) unique,
            email varchar(50),
            password varchar(25))""")

        self.cur.execute("""INSERT INTO users(first_name,last_name,username,email,password)
                values(?,?,?,?,?)""",(firstname,lastname,username,email,password))

        self.createProfile(username)

        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def createProfile(self,username):

        with open(media,"rb") as image:
            default_image = image.read()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS Profile (profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username varchar(20) UNIQUE,
            profile_pic BLOB not null,
            FOREIGN KEY (profile_id) REFERENCES users(user_id))""")

        self.cur.execute("""INSERT INTO users(username,profile_pic)
            values(?,?)""",(username,default_image))
 
    def validateUser(self,username,password):
        self.cur.execute(f""" SELECT username,password FROM users WHERE
            EXISTS(SELECT * FROM users WHERE username = '{username}' OR email='{username}')""")

        user = self.cur.fetchone()

        if user is not None and password in user:
            return True

        self.conn.commit()
        self.cur.close()
        self.conn.close()

        return False

    def UserValidation(self,username):
        try:
            self.cur.execute(f""" SELECT EXISTS(SELECT username FROM users WHERE username = '{username}')""")

            usernames = self.cur.fetchone()[0]

            self.conn.commit()
            self.cur.close()
            self.conn.close()

            if usernames == 1:
                return True
            
            return False

        except OperationalError:
            return False