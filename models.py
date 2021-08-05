from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

IMG_URL = 'https://images.unsplash.com/photo-1613678431006-3f369f14a2d9?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=751&q=80'


class Pet (db.Model):
    """Model for setting up a new pet"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=IMG_URL)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)


def connect_db(app):
    """Connect this database to Flask app"""

    db.app = app
    db.init_app(app)
