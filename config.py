#database config
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@localhost:5432/plannerdb'
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
