import datetime
import os
import json
import sqlite3
from sqlite3 import Error
import dates as dt

nachname = "nachname"
vorname = "vorname"
klasse = "klasse"

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
    participants_sql = "SELECT id, name, vorname, klasse FROM participants_"+str(dt.current_year)+" WHERE name = ? order by ? asc;"
    cur.execute(participants_sql, participants)
    conn.commit()
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    return (r[0] if r else None) if one else r

def main(nachname):
    if os.path.exists("suchergebnis.json"):
      os.remove("suchergebnis.json")
    database = r"./austausch.db"
    
    conn = create_connection(database)
    participants = (nachname, "name")
    
    if conn is not None:
        with conn:
            participants_data = get_participants(conn, participants)
    else:
        print("Error! cannot create the database connection.")
        
    json_output = json.dumps(participants_data)
    with open("suchergebnis.json", "w") as outfile:
        outfile.write(json_output)

if __name__ == '__main__':
    main()
