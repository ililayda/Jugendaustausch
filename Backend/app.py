from flask import Flask, flash, redirect, render_template, request, session, abort # pip install Flask
import os
import bcrypt # CMD: "pip3 install bcrypt" & "pip3 install schedule"
import registration as rg
import admin_speicherung as ads
import login as lg
import Ausgabe as ag
import search as se
import Teilnehmerspeicherung as ts
import payment_bar as pb
import payment_online as po
import json
from json2html import * # pip install json2html

email = "email"
password = "password"
anrede = "anrede"
name = "name"
vorname = "vorname"
klasse = "klasse"
klassenleitung = "klassenleitung"
volljährig = 1
mobilfunknummer = "nr"
id = 1

app = Flask(__name__, template_folder='../HTML_Backend', static_folder='../static')

@app.route('/')
def home():
    if session.get('logged_in'):
        return render_template('homepage.html')
    elif session.get('logged_in_admin'):
        return render_template('adminmask.html')
    else:
        return render_template('index.html')

@app.route('/homepage')
def homepage():
    if session.get('logged_in'):
        return render_template('homepage.html')
    elif session.get('logged_in_admin'):
        return render_template('adminmask.html')
    else:
        return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():

    emailForm = request.form['email']
    passwordForm = request.form['password']

    if passwordForm == 'admin' and emailForm == 'DEV':
        session['logged_in'] = True
    else:
        pw = False

        print(emailForm, passwordForm)

        user_obj = lg.give_user(emailForm)
        emailDB = user_obj[0]
        passwordDB = user_obj[1]
        print(emailDB, passwordDB)

        # Use conditions to compare the authenticating password with the stored one:
        passwordForm = passwordForm.encode('utf-8')

        if bcrypt.checkpw(passwordForm, passwordDB):
            print("password matches")
            pw = True
        else:
            print("incorrect password")

        if pw == True and (emailForm.__contains__(emailDB)):
            session['logged_in'] = True
        else:
            flash('Falsche Anmeldedaten!')
        return home()

    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['logged_in_admin'] = False
    return home()

@app.route("/registration")
def registration():
    return render_template('registration.html')

@app.route("/post_field_reg_user", methods=["POST"])
def get_user_data():
    for key, value in request.form.items():
        if key == "email":
            email = value
        elif key == "password":
            password = value
    rg.main(email, password)
    return render_template('login.html')

@app.route("/adminlogin") #admin login html
def adminlogin():
    return render_template('adminlogin.html')

@app.route("/post_field_login_admin", methods=["POST"]) #admin login
def get_admin_data():

    emailForm = request.form['email']
    passwordForm = request.form['password']
    nameForm = request.form['name']
    surnameForm = request.form['surname']

    if passwordForm == 'admin' and emailForm == 'j.buschmann' and nameForm == "J" and surnameForm == "Buschmann":
        session['logged_in_admin'] = True
    else:
        pw = False

        print(emailForm, passwordForm, nameForm, surnameForm)

        user_obj = lg.give_admin(emailForm)
        emailDB = user_obj[0]
        passwordDB = user_obj[1]
        nameDB = user_obj[2]
        surnameDB = user_obj[3]
        print(emailDB, passwordDB)

        # Use conditions to compare the authenticating password with the stored one:
        passwordForm = passwordForm.encode('utf-8')

        if bcrypt.checkpw(passwordForm, passwordDB):
            print("password matches")
            pw = True
        else:
            print("incorrect password")

        if pw == True and (emailForm.__contains__(emailDB)) and (nameForm.__contains__(nameDB)) and (surnameForm.__contains__(surnameDB)):
            session['logged_in_admin'] = True
            return render_template("adminmask.html")
        else:
            flash('Falsche Anmeldedaten!')
    return home()


@app.route("/post_field_reg_admin", methods=["POST"]) #admin_speicherung
def save_admin_data():
    session['logged_in_admin'] = True
    for key, value in request.form.items():
        if key == "surname":
            name = value
        elif key == "name":
            vorname = value
        elif key == "email":
            email = value
        elif key == "password":
            password = value
    ads.main(name, vorname, email, password)
    return homepage()

@app.route("/adminreg") #admin maske html
def adminreg():
    if session.get('logged_in_admin'):
        session['logged_in_admin'] = True
        return render_template('adminregister.html')
    elif session.get('logged_in'):
        return render_template('homepage.html')
    else:
        return render_template('index.html')

@app.route("/adminmask") #admin maske html
def adminmask():
    if session.get('logged_in_admin'):
        session['logged_in_admin'] = True
        return render_template('adminmask.html')
        get_all_participants()
    elif session.get('logged_in'):
        return render_template('homepage.html')
    else:
        return render_template('index.html')

@app.route("/participants") #admin maske html
def participants():
    if session.get('logged_in_admin'):
        session['logged_in_admin'] = True
        return render_template('participants.html')
    elif session.get('logged_in'):
        return render_template('homepage.html')
    else:
        return render_template('index.html')

@app.route("/reg_au") #austausch registrierung html
def participant_reg():
    return render_template('registrationexchange.html')

@app.route("/post_field_reg_au", methods=["POST"]) #Teilnahme-Formular
def get_participant_data():
    for key, value in request.form.items():
            if key == "surname":
                name = value
            elif key == "name":
                vorname = value
            elif key == "anrede":
                anrede = value
            elif key == "class":
                klasse = value
            elif key == "classT":
                klassenleitung = value
            elif key == "mobile":
                mobilfunknummer = value
            elif key == "age":
                volljährig = value
            elif key == "email":
                email = value
    ts.main(anrede, name, vorname, klasse, klassenleitung, mobilfunknummer, volljährig, email)
    return homepage()

@app.route("/get_field_partList", methods=["GET"]) #teilnehmerliste ausgeben
def get_all_participants():
    ag.main()  # erstellt die Datei teilnehmerliste.json, die muss ausgelesen werden

    data = open('teilnehmerliste.json', "r")
    jsonFile = data.read()
    foo = json.loads(jsonFile)
    html = json2html.convert(foo)

    with open('../HTML_Backend/participantList.html', "w") as ht:
        ht.write(html)

    return render_template('participantList.html')

@app.route("/post_field_user_search", methods=["POST"]) #suche nach teilnehmern
def get_search_():
    for key, value in request.form.items():
            if key == "name":
                name = value
    se.main(name) #erstellt die Datei suchergebnis.json, die muss ausgelesen werden

@app.route("/post_field_cash_edit", methods=["POST"]) # veränderung
def get_id_for_payment():
    for key, value in request.form.items():
        if key == "id":
            id = value
        elif key == "hat_bar_bezahlt":
            hat_bar_bezahlt = value
        elif key == "hat_online_bezahlt":
            hat_online_bezahlt = value

    if hat_bar_bezahlt == 1:
        pb.main(id)

    if hat_online_bezahlt == 1:
        po.main(id)

    return homepage()



    # HTML FÜR ENGLISCH ###############################################################################################






if __name__ == "__main__":
    app.secret_key = os.urandom(12)
app.run(debug=True,host='0.0.0.0', port=4000)
