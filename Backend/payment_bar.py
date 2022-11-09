import datetime
import sqlite3
from sqlite3 import Error
import dates as dt
import flask
from flask import Flask, request

id = 3
    
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

def has_payed(conn, payment_info):
    
    sql = "SELECT user_id from payment WHERE user_id = ? AND hat_bar_bezahlt = ? and hat_online_bezahlt = ?; "
    cur = conn.cursor()
    cur.execute(sql, payment_info)
    payed_participant = cur.fetchall()
    return payed_participant

def double_payment(conn, participant):
    
    sql = "UPDATE participants_"+str(dt.current_year)+" SET hat_bezahlt = ? WHERE id = ?; "
    cur = conn.cursor()
    cur.execute(sql, participant)
    conn.commit()

def insert_bar_payment(conn, payment):
    
    sql = "INSERT INTO payment(user_id, datum, hat_bar_bezahlt) VALUES (?, ?, 1); "
    cur = conn.cursor()
    cur.execute(sql, payment)
    conn.commit()

def main():
    database = r"./austausch.db"
    
    conn = create_connection(database)
    
    if conn is not None:
        with conn:
            payment = (id, dt.today)
            participant = (1, id)
            payment_info = (id, 1, 1)
            insert_bar_payment(conn, payment)
            is_payed = has_payed(conn, payment_info)
            if is_payed == id:
                double_payment(conn, participant)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()