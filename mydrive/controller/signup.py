from mydrive.webApp import app
from flask import render_template , request , flash , redirect ,url_for
from werkzeug.security import generate_password_hash, check_password_hash
from mydrive.models.user_model import Users
from mydrive.webApp import db
from flask_login import  current_user 


@app.route("/signup" )
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('display_all'))

    return render_template("signup.html" , title="SignUp - myDrive")

@app.route("/signup" , methods=["POST"])
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')

    checkValid = Users.query.filter_by(email=email).first()
    if checkValid:
        # print("Email exits")
        flash('Email address already exists')
        return redirect(url_for('signup'))

    password_hash = generate_password_hash(password , method='sha256')
    new_user = Users(name=name , email=email , password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()
    flash('SuccessFully Added !')
    # print(email)
    return redirect(url_for('login'))