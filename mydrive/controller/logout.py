from mydrive.webApp import app
from flask import render_template , request , flash , redirect , url_for
from werkzeug.security import generate_password_hash, check_password_hash
from mydrive.models.user_model import Users
from mydrive.webApp import db
from flask_login import login_user , login_required ,logout_user , current_user


@app.route("/logout")
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('home'))