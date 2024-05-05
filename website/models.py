from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Attribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(150))
    calorie_intake = db.Column(db.Float)
    water_intake = db.Column(db.Float)
    weight_goal = db.Column(db.Float)



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    Attributes = db.relationship('Attribute')    

class food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    apple = 52
    chicken = 299
    brocolli = 68
    meat = 215
    egg = 142
    banana = 105 
    orange = 45