from flask import Flask
from sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from app import routes


