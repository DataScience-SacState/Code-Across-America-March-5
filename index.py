from flask import Flask, render_template, flash
import flask.ext.login as flask_login
import flask
import os
import csv
import pprint

app = Flask(__name__)




if __name__ == '__main__':
    app.debug = True
    app.run()
