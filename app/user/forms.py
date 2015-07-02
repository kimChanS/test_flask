# coding:utf8
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import Required, Email

from .models import User

class LoginForm(Form):
    username = StringField('username:', validators=[Required()])
    email = StringField('email:', validators=[Required(), Email()])
    remember_me = BooleanField('Remember_me:')

    def get_user(self):
        return User.query.filter_by(username=self.username.data,
                                    email=self.email.data).first()
