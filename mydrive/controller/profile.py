from mydrive.webApp import app
from flask import render_template, request, flash, url_for, redirect, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from mydrive.models.user_model import Users
from mydrive.models.files_model import Files
from mydrive.webApp import db
from flask_login import login_required, current_user


@app.route("/view/<filename>", methods=["POST"])
def view_image(filename):
    return send_from_directory(directory=app.config['UPLOAD_FOLDER'], filename=filename)


@app.route("/download/<filename>", methods=["POST"])
def download_file(filename):
    return send_from_directory(directory=app.config['UPLOAD_FOLDER'], filename=filename,  as_attachment=True)


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    return render_template("profile.html", title="Welcome", name=current_user.name, current_user=current_user)


@app.route("/dashboard", methods=["GET"])
@login_required
def display_all():
    user_id = current_user.id
    data = Files.query.filter_by(user_id=user_id)
    # print(data.fileName)
    return render_template("profile.html", title="Welcome", name=current_user.name, data=data, test=1)
