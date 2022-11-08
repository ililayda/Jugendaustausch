import datetime
import sqlite3
from sqlite3 import Error
import dates as dt
import flask
from flask import Flask, request

email = "email"
password = "password"
    
app = Flask(__name__)

@app.route("/post_field", methods=["POST"])
def get_user_data():
    for key, value in request.form.items():
            if key == "email":
                    email = value
            elif key == "password":
                    password = value

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def insert_admin(conn, new_user):
    
    sql = "INSERT INTO users(email, password) VALUES(?, ?); "
    cur = conn.cursor()
    cur.execute(sql, new_user)
    conn.commit()

def main():
    database = r"./austausch.db"
    
    conn = create_connection(database)
    
    if conn is not None:
        with conn:
            new_user = (email, password)
            insert_admin(conn, new_user)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()