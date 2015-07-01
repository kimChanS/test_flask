# coding:utf8
from flask import Blueprint

from app.user.models import User

mod = Blueprint('app1_blueprint', __name__)

@mod.route('/')
def index():
    print User.query.all()
    return "hello app1"
