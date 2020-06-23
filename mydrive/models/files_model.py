from mydrive.webApp import db 
from datetime import datetime
from flask_login import UserMixin

class Files(UserMixin , db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer , primary_key=True)
    user_id = db.Column(db.Integer)
    filePath = db.Column(db.String(200))
    fileName = db.Column(db.String(200))
    fileExtension = db.Column(db.String(20))
    fileChecksum = db.Column(db.String(256) , index=True)
    fileSize = db.Column(db.Float)
    fileCreated = db.Column(db.DateTime , index=True ,default=datetime.utcnow)

    def __repr__(self):
        return 'id {}'.format(self.id)