from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


app = Flask(__name__)
app.config['SECRET_KEY'] = 'passwddev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:32281149@localhost:5432/plannerdb'

db = SQLAlchemy()
db.init_app(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

from app.models import User
from app import routes

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))







