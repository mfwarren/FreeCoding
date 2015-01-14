from flask import render_template
from flask.ext.login import login_required, current_user
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/nags')
@login_required
def nags():
    nags = current_user.nags
    return render_template('nags.html', nags=nags)
