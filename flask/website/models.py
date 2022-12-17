from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    
    id=db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(1000))
    date=db.Column(db.DateTime(timezone=True), default=func.now())
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    
     #time
    #date=db.Column(db.DateTime(timezone=True), default=func.now())
    
class Item(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(1000))
    types=db.Column(db.String(100)) #bfast lunch dinner
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp=db.Column(db.DateTime(timezone=True), default=func.now())
    
class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    notes=db.relationship('Note')