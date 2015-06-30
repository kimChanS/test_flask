# coding:utf8
from flask import Blueprint

mod = Blueprint('app1', __name__)

@mod.route('/')
def index():
    return "hello app1"
