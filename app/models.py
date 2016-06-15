from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import ARRAY

app = Flask(__name__)
db = SQLAlchemy(app)

class Picture (db.model):
    __tablename__="picture"
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.Unicode)
    latRef = db.Column('latRef', db.Unicode)
    longRef = db.Column('longRef', db.Unicode)
    longitude = db.Column('longitude', ARRAY(Float))
    latitude = db.Column('latitude', ARRAY(Float)   
    dateStamp = db.Column('dateStamp', db.Date, default=datetime.utcnow)



