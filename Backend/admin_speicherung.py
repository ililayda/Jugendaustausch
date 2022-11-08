import datetime
import sqlite3
from sqlite3 import Error
import dates as dt
import flask
from flask import Flask, request

email = "email"
password = "password"
name = "name"
vorname = "vorname"
    
app = Flask(__name__)

@app.route("/post_field", methods=["POST"])
def get_admin_data():
    for key, value in request.form.items():
            if key == "name":
                name = value
            elif key == "vorname":
                vorname = value
            elif key == "email":
                    email = value
            elif key == "vorname":
                    password = value

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def insert_admin(conn, new_admin):
    
    sql = "INSERT INTO admins(superadmin, email, password, name, vorname) VALUES(?, ?, ?, ?, ?); "
    cur = conn.cursor()
    cur.execute(sql, new_admin)
    conn.commit()

def main():
    database = r"./austausch.db"
    
    conn = create_connection(database)
    
    if conn is not None:
        with conn:
            new_admin = (0, email, password, name, vorname)
            insert_admin(conn, new_admin)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()