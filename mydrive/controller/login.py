from mydrive.webApp import app
from flask import render_template , request , flash , redirect , url_for
from werkzeug.security import generate_password_hash, check_password_hash
from mydrive.models.user_model import Users
from mydrive.webApp import db
from flask_login import login_user , current_user  , logout_user
import os
@app.route("/login" , methods=["GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('display_all'))
    # print("yes")
    logout_user()
    return render_template("login.html" , title="Login - myDrive" , login = False)

@app.route("/login" , methods=["POST"])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = Users.query.filter_by(email=email).first()

    print(email)
    # print(user.password_hash)
    if not user or not check_password_hash(user.password_hash , password):
        flash("Please check you Login details")
        return render_template("login.html" , signup=True)
    # print(email)
    # print("Success !")
    login_user(user , remember)
    # flash("login")
    return redirect(url_for('display_all'))

    # return render_template('login.html' , title="login - myDrive")


