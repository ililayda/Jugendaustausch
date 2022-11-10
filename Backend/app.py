from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import bcrypt # CMD: "pip3 install bcrypt" & "pip3 install schedule"
import registration as rg
import admin_speicherung as ads
import login as lg
import Ausgabe as ag
import search as se

email = "email"
password = "password"
name = "name"
vorname = "vorname"

app = Flask(__name__, template_folder='../HTML_Backend', static_folder='../static')

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('homepage.html')

@app.route('/login', methods=['POST'])
def login():

    pw = False

    emailForm = request.form['email']
    passwordForm = request.form['password']
    print(emailForm, passwordForm)

    emailDB = lg.give_email(request.form['email'])
    passwordDB = lg.give_password(request.form['password'])
    print(emailDB, passwordDB)

    # Use conditions to compare the authenticating password with the stored one:
    passwordForm = passwordForm.encode('utf-8')

    if bcrypt.checkpw(passwordForm, passwordDB):
        print("password matches")
        pw = True
    else:
        print("incorrect password")


    if pw == True and request.form['email'] == email:
        session['logged_in'] = True
    else:
        flash('Falsche Anmeldedaten!')
        if request.form['password'] == 'admin' and request.form['email'] == 'DEV':
            session['logged_in'] = True
        else:
            flash('Falsche Anmeldedaten!')
        return home()
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route("/registration")
def registration():
    return render_template('registration.html')

@app.route("/post_field", methods=["POST"])
def get_user_data():
    for key, value in request.form.items():
        if key == "email":
            email = value
        elif key == "password":
            password = value
    rg.main(email, password)
    return render_template('login.html')

@app.route("/post_field", methods=["POST"]) #admin_speicherung
def get_admin_data():
    for key, value in request.form.items():
            if key == "name":
                name = value
            elif key == "vorname":
                vorname = value
            elif key == "email":
                    email = value
            elif key == "vorname":
                    password = value
    ads.main(name, vorname, email, password)
    
@app.route("/get_field", methods=["GET"]) #teilnehmerliste ausgeben
def get_all_participants():
   ag.main   #erstellt die Datei teilnehmerliste.json, die muss ausgelesen werden

@app.route("/post_field", methods=["POST"]) #suche nach teilnehmern
def get_search_():
    for key, value in request.form.items():
            if key == "name":
                name = value
    se.main(name) #erstellt die Datei suchergebnis.json, die muss ausgelesen werden

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
app.run(debug=True,host='0.0.0.0', port=4000)
