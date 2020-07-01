from mydrive.webApp import app
from flask import render_template ,redirect , url_for
from flask_login import current_user 


@app.route("/")
def home():

    if current_user.is_authenticated:
        return render_template("home.html" , login =True)

    return render_template("home.html" , login=False)


@app.route("/about")
def about():
    if current_user.is_authenticated:
        return render_template("about.html" , login=True)
    
    return render_template("about.html" , login=False)



@app.route("/contact-us")
def contact():
    if current_user.is_authenticated:
        return render_template("contact.html" , login=True)
    
    return render_template("contact.html" , login=False)
