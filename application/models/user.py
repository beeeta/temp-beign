from flask_login import UserMixin
from . import db
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


    def get_id(self):
        return self.id
    