from flask import render_template, redirect, session, url_for, flash
from .. import db
from ..models import User
from . import main
from .forms import LoginForm, SignupForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.data.email).first()
        if user is None:
            flash('Login Failed!')
            return redirect(url_for('.index'))
    return render_template('index.html', form=form)


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.data.email).first()
        if user is None:
            user = User(username=form.data.email, password=form.data.password)
            db.session.add(user)
        else:
            flash('user with this name already exists')
    return render_template('signup.html', form=form)
