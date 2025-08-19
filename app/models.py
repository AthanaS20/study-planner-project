from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from __init__ import db

class User(db.Model, UserMixin):
    
