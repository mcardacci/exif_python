from exify import app 
from models import db
from models import User
from passlib.hash import sha256_crypt

users={"admin": "password", "charlie": "mingus", "lucile": "asdf"}

for user, password in users.items():
    encrypted_pass=sha256_crypt.encrypt(password)
    curr_user=User(user, encrypted_pass)
    db.session.add(curr_user)

db.session.commit()


