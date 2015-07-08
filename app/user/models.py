# coding:utf8
from flask_user import UserMixin, SQLAlchemyAdapter, UserManager
from app import app, db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication information
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    reset_password_token = db.Column(db.String(100), nullable=False, server_default='')

    # User Email information
    email = db.Column(db.String(255), nullable=False, unique=True, server_default='')
    confirmed_at = db.Column(db.DateTime())

    # User information
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')
    first_name = db.Column(db.String(50), nullable=False, server_default='')
    last_name = db.Column(db.String(50), nullable=False, server_default='')

    def is_active(self):
        return self.active


db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)
