# coding:utf8
from flask import Flask, url_for, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)

from .app1.app1 import mod as app1
from .app2.app2 import mod as app2
from .user.user import mod as user
from .user.models import User as userModel

app.register_blueprint(app1, url_prefix='/app1')
app.register_blueprint(app2, url_prefix='/app2')
app.register_blueprint(user, url_prefix='/user')

admin = Admin(app, name='My app')
admin.add_view(ModelView(userModel, db.session, name='chj'))

login_manager.login_view = "user_blueprint.login"

@app.route('/')
def index():
    print(url_for('index'))
    print(url_for('app1_blueprint.index'))
    print(url_for('app2_blueprint.index'))
    return render_template('index.html')
