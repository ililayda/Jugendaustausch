import datetime
import sqlite3
from sqlite3 import Error
import dates as dt
import flask
from flask import Flask

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def insert_participant(conn, new_participant):

    sql = "INSERT INTO participants_"+str(dt.current_year)+"(datum, anrede, name, vorname, klasse, klassenleitung, mobilfunknummer, volljaehrig, email, hat_bezahlt) VALUES(?,?,?,?,?,?,?,?,?,?);"
    cur = conn.cursor()
    cur.execute(sql, new_participant)
    conn.commit()

def main(anrede, name, vorname, klasse, klassenleitung, mobilfunknummer, volljährig, email):
    database = r"./austausch.db"
    
    conn = create_connection(database)
    
    if conn is not None:
        with conn:
            new_participant = (str(dt.today), anrede, name, vorname, klasse, klassenleitung, mobilfunknummer, volljährig, email ,0)
            insert_participant(conn, new_participant)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
