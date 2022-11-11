import datetime
import os
import json
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

def get_participants(conn, participants, one=False):

    cur = conn.cursor()
    cur.execute(participants)
    conn.commit()
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    return (r[0] if r else None) if one else r

def main():
    if os.path.exists("teilnehmerliste.json"):
      os.remove("teilnehmerliste.json")
    database = r"./austausch.db"
    
    conn = create_connection(database)
    participants = "SELECT * FROM participants_"+str(dt.current_year)+";"
    
    if conn is not None:
        with conn:
            participants_data = get_participants(conn, participants)
    else:
        print("Error! cannot create the database connection.")
        
    json_output = json.dumps(participants_data)
    with open("teilnehmerliste.json", "w") as outfile:
        outfile.write(json_output)


if __name__ == '__main__':
    main()