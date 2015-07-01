# coding:utf8
from flask import Blueprint

mod = Blueprint('app2_blueprint', __name__)

@mod.route('/')
def index():
    return "Hello app2"
