from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(300), nullable=False)
    last_name = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(300), nullable=False, unique=True)
    password = db.Column(db.String(700), nullable=False)
    createteam = db.relationship('CreateTeam', backref='author', lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)

class CreateTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poke1 = db.Column(db.String(100), nullable=False)
    poke2 = db.Column(db.String(100), nullable=False)
    poke3 = db.Column(db.String(100), nullable=False)
    poke4 = db.Column(db.String(100), nullable=False)
    poke5 = db.Column(db.String(100), nullable=False)
    poke6 = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, poke1, poke2, poke3, poke4, poke5, poke6, user_id):
        self.poke1 = poke1
        self.poke2 = poke2
        self.poke3 = poke3
        self.poke4 = poke4
        self.poke5 = poke5
        self.poke6 = poke6
        self.user_id = user_id

