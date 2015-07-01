# coding:utf8
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'test.db')

SECRET_KEY = 'sdfkjwlerjwejr'
