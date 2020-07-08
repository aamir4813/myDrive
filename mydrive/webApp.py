from flask import Flask
from mydrive.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

import os

app = Flask(__name__)

# for login management
# login = LoginManager(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

app.config.from_object(Config)
DB_USER = os.environ.get('DB_NAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
# print(DB_NAME)
# app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] =  "mysql+pymysql://drive:myDrive#123@localhost:3306/mydrive"
# app.config['SQLALCHEMY_DATABASE_URI'] =  "mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost:3306/{DB_NAME}"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


import mydrive.controller.profile
import mydrive.controller.home 
import mydrive.controller.login
import mydrive.controller.signup
import mydrive.controller.logout
import mydrive.controller.upload
# import mydrive.controller


from mydrive.models.user_model import Users
from mydrive.models.files_model import Files

@login_manager.user_loader
def load_user(users_id):
    return Users.query.get(int(users_id))

# db.create_all()

# db.commit()