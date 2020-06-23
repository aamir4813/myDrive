from mydrive.webApp import app
from flask import render_template , request , flash , redirect , url_for
from werkzeug.security import generate_password_hash, check_password_hash
from mydrive.models.user_model import Users
from mydrive.webApp import db
from flask_login import login_user , current_user 

@app.route("/login" , methods=["GET"])
def login():
   
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    return render_template("login.html" , title="Login - myDrive")

@app.route("/login" , methods=["POST"])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = Users.query.filter_by(email=email).first()
   
    # print(user.password_hash)
    if not user or not check_password_hash(user.password_hash , password):
        flash("Please check you Login details")
        return redirect(url_for('login'))
    # print(email)
    # print("Success !")
    login_user(user , remember)
    return redirect(url_for("profile"))

    # return render_template('login.html' , title="login - myDrive")


