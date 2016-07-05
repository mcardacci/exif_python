from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON, JSONB

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://marco:mypass@localhost/exify'
db = SQLAlchemy(app)

class Picture (db.Model):
    __tablename__="picture"
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.Unicode)
    latRef = db.Column('latRef', db.Unicode)
    longRef = db.Column('longRef', db.Unicode)
    longitude = db.Column('longitude',JSON)
    latitude = db.Column('latitude', JSON)   
    dateStamp = db.Column('dateStamp', db.Date, default=datetime.utcnow)

class User(db.Model):
    __tablename__="users"
    
    id = db.Column('id', db.Integer, primary_key=True)
    username=db.Column('username', db.Unicode)
    password=db.Column('password', db.Unicode)

    def __init__(self, username, password):
        self.username=username
        self.password=password
