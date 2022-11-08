import datetime
import sqlite3
from sqlite3 import Error
import dates as dt
import flask
from flask import Flask, request

id = 1
    
app = Flask(__name__)

@app.route("/post_field", methods=["POST"])
def get_id():
    for key, value in request.form.items():
            if key == "id":
                id = value

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def insert_payment(conn, payment):
    
    sql = "UPDATE participants_"+str(dt.current_year)+" SET hat_bezahlt = ? WHERE id = ?; "
    cur = conn.cursor()
    cur.execute(sql, payment)
    conn.commit()

def main():
    database = r"./austausch.db"
    
    conn = create_connection(database)
    
    if conn is not None:
        with conn:
            payment = (1, id)
            insert_payment(conn, payment)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()