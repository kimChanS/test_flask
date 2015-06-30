# coding:utf8
from flask import Flask, url_for
from app1.app1 import mod as app1
from app2.app2 import mod as app2
from user.user import mod as user

app = Flask(__name__)
app.register_blueprint(app1, url_prefix='/app1')
app.register_blueprint(app2, url_prefix='/app2')
app.register_blueprint(user, url_prefix='/user')

@app.route('/')
def index():
    print url_for('index')
    print url_for('app1.index')
    print url_for('app2.index')
    return "Hello main app."

if __name__ == '__main__':
    app.run(debug=True)
