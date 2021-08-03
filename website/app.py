# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')
@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/page4')
def page4():
    return render_template('page4.html')

@app.route('/results', methods=['GET','POST'])
def results():
    username = request.form['contact']
    return render_template('results.html', contact_information=username)

