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

def delete_participant(conn, old_date):

    sql = "DElETE FROM participants_"+str(dt.current_year)+" WHERE date(datum) = ? AND hat_bezahlt = ?; "
    cur = conn.cursor()
    cur.execute(sql, old_date)
    conn.commit()

def main():
    database = r"./austausch.db"
    
    conn = create_connection(database)
    
    if conn is not None:
        with conn:
            old_date = (str(dt.fourteen_days_ago), 0)
            delete_participant(conn, old_date)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()