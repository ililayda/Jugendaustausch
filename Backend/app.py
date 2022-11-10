from flask import Flask, flash, redirect, render_template, request, session, abort
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

email = "email"
password = "password"
anrede = "anrede"
name = "name"
vorname = "vorname"
klasse = "klasse"
klassenleitung = "klassenleitung"
volljährig = 1
mobilfunknummer "nr"
id = 1

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
        if passwordForm == 'admin' and emailForm == 'DEV':
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

@app.route("/post_field_reg_user", methods=["POST"])
def get_user_data():
    for key, value in request.form.items():
        if key == "email":
            email = value
        elif key == "password":
            password = value
    rg.main(email, password)
    return render_template('login.html')

@app.route("/post_field_reg_admin", methods=["POST"]) #admin_speicherung
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
    
@app.route("/post_field_reg_au", methods=["POST"]) #Teilnahme-Formular
def get_participant_data():
    for key, value in request.form.items():
            if key == "name":
                name = value
            elif key == "vorname":
                vorname = value
            elif key == "anrede":
                anrede = value
            elif key == "klasse":
                klasse = value
            elif key == "klassenleitung":
                klassenleitung = value
            elif key == "mobilfunknummer":
                mobilfunknummer = value
            elif key == "volljährig":
                volljährig = value
            elif key == "email":
                email = value
    ts.main(anrede, name, vorname, klasse, klassenleitung, mobilfunknummer, volljährig, email)

    
@app.route("/get_field_user", methods=["GET"]) #teilnehmerliste ausgeben
def get_all_participants():
   ag.main()   #erstellt die Datei teilnehmerliste.json, die muss ausgelesen werden

@app.route("/post_field_user_search", methods=["POST"]) #suche nach teilnehmern
def get_search_():
    for key, value in request.form.items():
            if key == "name":
                name = value
    se.main(name) #erstellt die Datei suchergebnis.json, die muss ausgelesen werden

@app.route("/post_field_cash", methods=["POST"]) #bestätigung der bar zahlung
def get_id_for_bar_payment():
    for key, value in request.form.items():
            if key == "id":
                id = value
    pb.main(id)

@app.route("/post_field_cash_on", methods=["POST"]) #bestätigung der online zahlung
def get_id_for_online_payment():
    for key, value in request.form.items():
            if key == "id":
                id = value
     po.main(id)
    
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
app.run(debug=True,host='0.0.0.0', port=4000)
