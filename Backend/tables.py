import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"./austausch.db"

    sql_create_participants_table = """ CREATE TABLE IF NOT EXISTS participants_2022 (
                                        id integer PRIMARY KEY,
                                        datum text,
                                        anrede text,
                                        name text,
                                        vorname text,
                                        klasse text,
                                        klassenleitung text,
                                        mobilfunknummer text,
                                        volljährig integer,
                                        email text,
                                        hat_bezahlt integer 
                                    ); """

    sql_create_admins_table = """CREATE TABLE IF NOT EXISTS admins (
                                    id integer PRIMARY KEY,
                                    superadmin integer,
                                    email text,
                                    password text,
                                    name text,
                                    vorname text
                                );"""


    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, email text, password text);"""
    
    sql_create_zahlungs_table = " CREATE TABLE IF NOT EXISTS payment(user_id integer NOT NULL, datum NOT NULL, hat_bar_bezahlt integer, hat_online_bezahlt integer, PRIMARY KEY (user_id, datum), FOREIGN KEY(user_id) REFERENCES participants_"+str(dt.current_year)+"(id));"
    
    conn = create_connection(database)


    if conn is not None:

        create_table(conn, sql_create_participants_table)

        create_table(conn, sql_create_admins_table)
        
        create_table(conn, sql_create_users_table)
        
        create_table(conn, sql_create_zahlungs_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
