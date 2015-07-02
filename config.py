# coding:utf8
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'test.db')

SECRET_KEY = 'sdfkjwlerjwejr'

# recaptcha
RECAPTCHA_PUBLIC_KEY = "6lEyBSaaaCAKJWLEKRJ2344S3D4F SDF"
RECAPTCHA_PRIVATE_KEY = "6lESLKJFWLEKFJW EF-=-=WEF4V6FEE"
