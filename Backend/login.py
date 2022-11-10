import datetime
import bcrypt # CMD: "pip3 install bcrypt" & "pip3 install schedule"
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

def get_user(conn, email):

    cur = conn.cursor()

    emailS = cur.execute('SELECT email FROM users WHERE email = ?;', (email,))
    email = cur.fetchone(emailS)
    passwordS = cur.execute('SELECT password FROM users WHERE email = ?;', (email,))
    password = cur.fetchone(passwordS)
    conn.commit()

    print(email, password)

    user_obj = (email, password)

    return user_obj

def give_user(email):
    database = r"./austausch.db"

    conn = create_connection(database)

    if conn is not None:
        with conn:
            return get_user(conn, email)
    else:
        print("Error! cannot check the database connection.")

def main():
    database = r"./austausch.db"

    conn = create_connection(database)

    if conn is not None:
        with conn:
            print("Connected.")
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
