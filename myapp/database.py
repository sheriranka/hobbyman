from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Stats(db.Model):
    activity = db.Column(db.Text)
    time_spent = db.Column(db.Text)
