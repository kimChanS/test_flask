# coding:utf8
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'test.db')

SECRET_KEY = 'sdfkjwlerjwejr'

DEBUG = True

# mail
MAIL_USERNAME = '120831629'
MAIL_PASSWORD = 'password'
MAIL_DEFAULT_SENDER = '"Sender" <120831629@qq.com>'
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USER_SSL = True
MAIL_USER_TLS = False
