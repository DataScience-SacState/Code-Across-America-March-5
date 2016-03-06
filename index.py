from flask import Flask, render_template, flash, request, redirect
from flask.ext.wtf import Form
import flask.ext.login as flask_login
from wtforms import TextField
from wtforms.validators import Required, Length, ValidationError
import os
import csv
import pprint

app = Flask(__name__)

class LoginForm(Form):
    fname = TextField('fname')
    lname = TextField('lname')

def blah(name):
    return str('hame')

@app.route('/', methods=['GET','POST'])
def index():
    form = LoginForm(request.form, csrf_enabled = False)
    if form.validate_on_submit():
        return blah(form.data['fname'])
    return render_template('index.html', title = "afd", form = form)

'''
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')
'''

if __name__ == '__main__':
    app.debug = True
    app.run()

