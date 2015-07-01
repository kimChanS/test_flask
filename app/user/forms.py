# coding:utf8
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Required, Email

from .models import User

class LoginForm(Form):
    username = StringField('username', validators=[Required()])
    email = StringField('email', validators=[Required(), Email()])

    def get_user(self):
        return User.query.filter_by(username=self.username.data,
                                    email=self.email.data).first()
