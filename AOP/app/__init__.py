from flask import Flask, redirect, url_for, escape, request, render_template, \
    logging, session
import os

# from jinja2 import render_template
app = Flask(__name__)
app.secret_key = 'rainer010'

@app.route('/')
def raiz():
    esta_logeado()
    return redirect(url_for('login'))
    

@app.route('/login', methods=['GET', 'POST'])   
def login():
    if request.method == 'POST':
        session['logged_in']=True
        return redirect(url_for('menu'))
    if 'logged_in' in session:
        if session['logged_in']==True:
            return redirect(url_for('menu')) 
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])   
def logout():
    session['logged_in']=False
    return redirect(url_for('login'))

@app.route('/menu')   
def menu():
    if not esta_logeado():
        return redirect(url_for('login'))
    return render_template('child.html')

def esta_logeado():
    if 'logged_in' in session:
        if session['logged_in']==True:
            return True
    return False

if __name__ == '__main__':
   app.run(debug=True)

