from mydrive.webApp import app
from flask import render_template

@app.route("/" , methods=["GET"] )
def home():
    return render_template('home.html' , title="myDrive-Home")