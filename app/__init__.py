from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin


app = Flask(__name__)
app.config['SECRET_KEY'] = 'passwddev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'

db = SQLAlchemy(app)
#login_manager = LoginManager(app)

from app import routes




