import flask
from flask import flash, session, render_template, request, redirect, Flask
import sqlite3
from sqlite3 import Error

@app.route('/')
def index():
    if 'email' in session:
        email = session['email']
        return render_template("../HTML/index.html")
    return render_template("../HTML/login.html")

@app.route('/login')
def login():
    return render_template('../HTML/login.html')

@app.route('/submit', methods=['POST'])
def login_submit():
    _email = request.form['email']
    _password = request.form['password']
    # validate the received values
    if _email and _password and request.method == 'POST':
        #check user exists
        database = r"./austausch.db"
        conn = create_connection(database)
        cursor = conn.cursor()
        sql = "SELECT * FROM users WHERE email=%s" # PRÜFEN
        sql_where = (_email,)
        cursor.execute(sql, sql_where)
        row = cursor.fetchone()
        if row:
            rowS = str(row[2])
            if rowS == _password:
                session['email'] = row[1]
                cursor.close()
                conn.close()
                return redirect('../HTML/homepage.html')
            else:
                flash('Invalid password!')
                return redirect('/login')
        else:
            flash('Invalid email/password!')
            return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/')

def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
    return conn


if __name__ == "__main__":
    app.run()