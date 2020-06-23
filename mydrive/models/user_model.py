from mydrive.webApp import db
from datetime import datetime
from flask_login import UserMixin


class Users(UserMixin , db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    lastLogin = db.Column(db.DateTime , default=datetime.utcnow )

    

    def __repr__(self):
        return 'email {}'.format(self.email)