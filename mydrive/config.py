import os

class Config(object):
    # SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('TRACK_VALUE')
    SQLALCHEMY_ECHO = True
    SECRET_KEY = "thisismysecret"
    DEBUG = True
    UPLOAD_FOLDER=os.getcwd() + ("/Storage")
    