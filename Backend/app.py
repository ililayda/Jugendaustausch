from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__, template_folder='../HTML')

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('homepage.html')

@app.route('/login', methods=['POST'])
def do_login():
    if request.form['password'] == 'password' and request.form['email'] == 'email':
        session['logged_in'] = True
    else:
        flash('Falsches Passwort!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
app.run(debug=True,host='0.0.0.0', port=4000)