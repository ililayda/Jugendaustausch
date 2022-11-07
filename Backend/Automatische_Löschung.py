import datetime
import sqlite3
from sqlite3 import Error
import dates as dt

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def delete_participant(conn, old_participant):

    sql = "DElETE FROM participants_"+str(dt.three_years_ago)+" WHERE strftime('%d', datum) = ? AND strftime('%m', datum) = ? AND strftime('%Y', datum) = ?; "
    cur = conn.cursor()
    cur.execute(sql, old_participant)
    conn.commit()

def main():
    database = r"./austausch.db"
    
    conn = create_connection(database)
    
    if conn is not None:
        with conn:
            old_participant = (str(dt.current_day), str(dt.current_month), str(dt.three_years_ago))
            delete_participant(conn, old_participant)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()