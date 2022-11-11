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
    sql = 'SELECT email, password FROM users WHERE email LIKE ?;'
    result = cur.execute(sql, (email,))

    line = result.fetchone()
    email = line[0]
    password = line[1]

    print(email)
    print(password)

    if not password: # An empty result evaluates to False.
        print("Login failed")
    else:
        print("Welcome")
        user_obj = (email, password)
        return user_obj


def get_admin(conn, email):

    print(email)
    cur = conn.cursor()
    sql = 'SELECT email, password, name, vorname FROM admins WHERE email LIKE ?;'
    result = cur.execute(sql, (email,))

    line = result.fetchone()
    email = line[0]
    password = line[1]
    name = line[2]
    vorname = line[3]

    print(email)
    print(password)

    if not password: # An empty result evaluates to False.
        print("Login failed")
    else:
        print("Welcome")
        user_obj = (email, password, name, vorname)
        return user_obj


def give_user(email):
    database = r"./austausch.db"

    conn = create_connection(database)

    if conn is not None:
        with conn:
            return get_user(conn, email)
    else:
        print("Error! cannot check the database connection.")

def give_admin(email):
    database = r"./austausch.db"

    conn = create_connection(database)

    if conn is not None:
        with conn:
            return get_admin(conn, email)
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