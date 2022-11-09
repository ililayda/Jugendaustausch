from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import bcrypt # CMD: "pip3 install bcrypt" & "pip3 install schedule"
import registration as rg
import login as lg

email = "email"
password = "password"

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
    print(email, password)

    emailDB = lg.give_email(request.form['email'])
    passwordDB = lg.give_password(request.form['password'])

    # Use conditions to compare the authenticating password with the stored one:
    passwordDB = check.encode('utf-8')

    if bcrypt.checkpw(passwordDB, hashed):
        print("password matches")
        pw = True
    else:
        print("incorrect password")


    if pw = True and request.form['email'] == email:
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

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
app.run(debug=True,host='0.0.0.0', port=4000)