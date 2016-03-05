from flask import Flask, render_template, flash
import flask.ext.login as flask_login
import flask
import os
import csv
import pprint

app = Flask(__name__)

@app.route('/', methods['GET','POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

