from sqlite3.dbapi2 import Cursor
import psycopg2
import psycopg2.extras
import os

cwd = os.path.split(__file__)[0]

media = os.path.join(os.path.split(__file__)[0],"media/profile_pics")
default_img = os.path.join(media,"default1.png")

class Database():
    def __init__(self):
        self.conn = psycopg2.connect(
            database="testdb",
            user="test",
            password="test123"
        )

        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)        

    def createUser(self,firstname,lastname,username,email,password):

        self.cur.execute("""CREATE TABLE IF NOT EXISTS users (user_id SERIAL primary key,
            first_name varchar(20),
            last_name varchar(20),
            username varchar(20) unique,
            email varchar(50),
            password varchar(25))""")

        self.cur.execute("""INSERT INTO users(first_name,last_name,username,email,password)
                values(%s,%s,%s,%s,%s)""",(firstname,lastname,username,email,password))

        self.createProfile(username)

        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def createProfile(self,username):

        with open(default_img,"rb") as image:
            default_image = image.read()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS Profile (profile_id SERIAL PRIMARY KEY,
            username varchar(20) UNIQUE,
            profile_pic bytea not null,
            FOREIGN KEY (profile_id) REFERENCES users(user_id))""")

        self.cur.execute("""INSERT INTO Profile(username,profile_pic)
            values(%s,%s)""",(username,default_image))
 
    def validateUser(self,username,password):
        self.cur.execute(f""" SELECT username,password FROM users WHERE username=%s OR email=%s """,(username,username))

        user = self.cur.fetchone()

        if user is not None and password in user:
            return True

        self.conn.commit()
        self.cur.close()
        self.conn.close()

        return False

    def UserValidation(self,username):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users (user_id SERIAL primary key,
        first_name varchar(20),
        last_name varchar(20),
        username varchar(20) unique,
        email varchar(50),
        password varchar(25))""")

        self.cur.execute(f""" SELECT username FROM users WHERE username=%s """,(username,))

        usernames = self.cur.fetchone()

        self.cur.close()
        self.conn.close()

        if usernames:
            return True
        
        return False