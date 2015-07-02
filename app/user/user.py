# coding:utf8
from flask import Blueprint, json, url_for, redirect, render_template, flash
from flask.ext.login import login_user, logout_user, login_required
from flask.views import MethodView

from app import login_manager
from .forms import LoginForm
from .models import User

mod = Blueprint('user_blueprint', __name__, template_folder="templates")

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

class UserAPI(MethodView):
    def get(self):
        users = [
            {'nickname': 'Chan'},
            {'nickname': 'Hzz'},
        ]
        return json.dumps(users)

mod.add_url_rule('/users/', view_func=UserAPI.as_view('users'))

@mod.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        remember_me = form.remember_me.data
        user = form.get_user()
        login_user(user, remember=remember_me)
        flash('Log in successfully')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@mod.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
