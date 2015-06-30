# coding:utf8
from flask import Blueprint

mod = Blueprint('app2', __name__)

@mod.route('/')
def index():
    return "Hello app2"
