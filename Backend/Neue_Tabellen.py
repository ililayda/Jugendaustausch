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


def create_table(conn, create_table_in_december):

    cur = conn.cursor()
    cur.execute(create_table_in_december)
    conn.commit()
    
def drop_table(conn, droped_table):

    cur = conn.cursor()
    cur.execute(droped_table)
    conn.commit()

def main():
    database = r"./austausch.db"
    
    conn = create_connection(database)
    
    create_table_in_december =  "CREATE TABLE IF NOT EXISTS participants_"+ str(dt.next_year)+"(id integer PRIMARY KEY,datum text,anrede text,name text,vorname text,klasse text,klassenleitung text,mobilfunknummer text,volljährig integer,hat_bezahlt integer );"
    droped_table = "DROP TABLE participants_"+str(dt.three_years_ago)
    if dt.current_month == '12':
        if conn is not None:
             with conn:
                 create_table(conn, create_table_in_december)
                 if dt.current_year - 3 == dt.three_years_ago:
                    drop_table(conn, droped_table)
        else:
            print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()