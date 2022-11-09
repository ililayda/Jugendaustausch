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

def check_email(conn, email):

    cur = conn.cursor()
    cur.execute('SELECT * email FROM users WHERE email = ?;', email)
    email = cur.fetchone()

    print(email)

    return email

def check_password(conn, password):

    cur = conn.cursor()
    cur.execute('SELECT password FROM users WHERE password = ?;', password)
    password = cur.fetchone()

    print(password)

    return password

def give_email(email):
    database = r"./austausch.db"

    conn = create_connection(database)

    if conn is not None:
        with conn:
            return check_email(conn, email)
    else:
        print("Error! cannot check the database connection.")

def give_password(password):
    database = r"./austausch.db"

    conn = create_connection(database)

    if conn is not None:
        with conn:
            return check_password(conn, password)
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
