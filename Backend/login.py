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

    print(email)
    cur = conn.cursor()
    sql = 'SELECT email, password FROM users WHERE email = ?;'
    cur.execute(sql, (email,))

    email = cur.fetchone()[0]
    password = cur.fetchone()[1]

    print(email)
    print(password)
    conn.commit()

    if not password:  # An empty result evaluates to False.
        print("Login failed")
    else:
        print("Welcome")
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