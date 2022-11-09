import datetime
import bcrypt # CMD: "pip3 install bcrypt"
import sqlite3
from sqlite3 import Error
import dates as dt
import flask
from flask import Flask, request

app = Flask(__name__)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def insert_user(conn, email, password):

    cur = conn.cursor()
    cur.execute('INSERT INTO users(email, password) VALUES(?, ?);', (email, password))
    result = cur.execute('SELECT * FROM users')
    conn.commit()

    print(cur.lastrowemail)

def main(email, password):

    database = r"./austausch.db"

    conn = create_connection(database)
    
    encoded_password = password.encode('utf-8')
    hashed = bcrypt.hashpw(encoded_password, bcrypt.gensalt(10)) 
    
    if conn is not None:
        with conn:
            insert_user(conn, email, hashed)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main("", "")
