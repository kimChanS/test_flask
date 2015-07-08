# coding:utf8
from flask import Blueprint
from flask_user import login_required

from app.user.models import User

mod = Blueprint('app1_blueprint', __name__)

@mod.route('/')
@login_required
def index():
    print(User.query.all())
    return "hello app1"
