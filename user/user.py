# coding:utf8
from flask import Blueprint, json
from flask.views import MethodView

mod = Blueprint('user', __name__)

class UserAPI(MethodView):
    def get(self):
        users = [
            {'nickname': 'Chan'},
            {'nickname': 'Hzz'},
        ]
        return json.dumps(users)

mod.add_url_rule('/users/', view_func=UserAPI.as_view('users'))
