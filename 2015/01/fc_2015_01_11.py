#!/usr/bin/env python3
# imports go here
import os

import gspread

from flask import Flask, redirect, render_template, url_for
from flask.ext.script import Manager
from flask.ext.login import LoginManager, login_user
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

from oauth2client.client import OAuth2WebServerFlow

#
# Free Coding session for 2015-01-11
# Written by Matt Warren
#

CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

app = Flask(__name__)
manager = Manager(app)
login_manager = LoginManager(app)

USER_GOOGLE_CREDENTIALS = None


class User:
    pass


class LoginForm(Form):
    name = StringField('Name', validators=[Required()])
    submit = SubmitField('Submit')


@login_manager.user_loader
def load_user(userid):
    return User()


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.data.name)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


def get_credentials():
    global USER_GOOGLE_CREDENTIALS
    if USER_GOOGLE_CREDENTIALS is None or USER_GOOGLE_CREDENTIALS.invalid:
        flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
                                   client_secret=CLIENT_SECRET,
                                   scope='https://spreadsheets.google.com/feeds https://docs.google.com/feeds',
                                   redirect_uri='http://localhost')
        return redirect(flow.step1_get_authorize_url())

    return USER_GOOGLE_CREDENTIALS


def booklist(name="Books"):
    gc = gspread.authorize(get_credentials())

    spreadsheet = gc.open(name)
    books = spreadsheet.sheet1.get_all_values()

    # convert to list of dictionaries using first row as keys
    books = [{books[0][i]: book[i] for i in range(len(books[0]))} for book in books[1:]]
    return books
