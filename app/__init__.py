from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from data_base_config import postgresql as settings


app = Flask(__name__)
app.config['SECRET_KEY'] = 'passwddev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:32281149@localhost:5432/plannerdb'

db = SQLAlchemy()
db.init_app(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

def get_engine(user, password, host, port, db):
    url = f"postgresql://{user}:{password}:{host}:{port}:{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

engine = get_engine(

    settings['pguser'],
    settings['password'],
    settings['pghost'],
    settings['pgport'],
    settings['pgdb'],
)

print(engine.url)

from app.models import User
from app import routes 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))






