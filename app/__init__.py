from flask import Flask

app = Flask(__name__)
# app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://marco:mypasss@    localhost/exify'

from app import views
