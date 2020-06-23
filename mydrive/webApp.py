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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://drive:myDrive#123@localhost:3306/mydrive'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


import mydrive.controller.profile
import mydrive.controller.home 
import mydrive.controller.login
import mydrive.controller.register
import mydrive.controller.logout
import mydrive.controller.upload


from mydrive.models.user_model import Users
from mydrive.models.files_model import Files

@login_manager.user_loader
def load_user(users_id):
    return Users.query.get(int(users_id))

db.create_all()

# db.commit()